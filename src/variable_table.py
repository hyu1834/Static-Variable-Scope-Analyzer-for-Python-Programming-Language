# Author: Hiu Hong Yu && Ming-Hung Lu
# University of California, Davis
# Winter 2017 - ECS 240 - Zhendong Su

#Standard Libraries
import re

#3rd Party Libraries
from enum import Enum

#Local Libraries
import undeclared_local_variable
import overriding_declared_variable
import global_local_variable_confusion
import function_parameter_overridden

class Operation(Enum):
	READ = 0
	WRITE = 1
	ASSIGN = 2
	ARG = 3


class Variable_Table:
	def __init__(self, source_code_filepath):
		# Dict for variable table
		self.variable_table = {}
		self.parse_code(source_code_filepath)

	def parse_arithmetic_expression(self, container, expression, indention, line_num, line):
		matcher = re.match(r'[ \t]*([A-Za-z0-9]+([ \t]*[-\+*][ \t]*[A-Za-z0-9]+)*)([ \t]*#?.*)$', expression)
		if(matcher):
			# replace all operator to , so we can split easily
			# for each item check if its variable name
			for variable_name in re.sub(r' ', '', re.sub(r'[-\+*]', ',', matcher.groups()[0])).split(','):
				try:
					# if just a number, ignore it
					float(variable_name)
				except ValueError:
					container.append((variable_name, Operation.READ, indention, line))

		return container

	def parse_boolean_expression(self, container, expression, indention, line_num, line):
		matcher = re.match(r'[ \t]*([A-Za-z0-9]+([ \t]*[<=>!]+[ \t]*[A-Za-z0-9]+)*)([ \t]*#?.*)$', expression)
		if(matcher):
			expression = matcher.groups()[0]
			# replace all comparsion operator to , so we can split easily
			for item in [r'==', r'<=', r'>=', r'!=', r'<', r'>']:
				expression = re.sub(item, ',', expression)

			# for each item check if its variable name
			for variable_name in re.sub(r' ', '', expression).split(','):
				try:
					# if just a number, ignore it
					float(variable_name)
				except ValueError:
					container.append((variable_name, Operation.READ, indention, line))
		
		return container

	def parse_function_expression(self, container, expression, indention, line_num, line):
		matcher = re.match(r'[ \t]*range\((.*),(.*)\)?([ \t]*#?.*)$', expression)
		if(matcher):
			for i in range(0, 2):
				try:
					# if just a number, ignore it
					float(matcher.groups()[i])
				except ValueError:
					container.append((matcher.groups()[i], Operation.READ, indention, line))

		return container


	def is_function_def(self, line_num, line, offset):
		# if it is a function defination
		matcher = re.match(r'([ \t]*)def ([A-Za-z0-9]+)(\(([A-Za-z0-9]*(,[ \t]*[A-Za-z0-9]+)*)\)):([ \t]*#?.*)\n$', line)
		if(matcher):
			indention = matcher.groups()[0].count('\t') + offset
			function_name = matcher.groups()[1]
			# break the function arguements string into list of variable names
			variables = re.sub(r' ', '', str(matcher.groups()[3])).split(',') if(matcher.groups()[2]) else []
			# construct line element by variables
			self.variable_table[line_num] = [(variable_name, Operation.ARG, indention, line) for variable_name in variables]
			return True

		return False

	def is_variable_assignment(self, line_num, line, offset):
		# Variable assignment
		matcher = re.match(r'([ \t]*)(.*)[ \t]*=[ \t]*(.*)([ \t]*#?.*)\n?$', line)
		if(matcher):
			indention = matcher.groups()[0].count('\t') + offset
			variables = re.sub(r' ', '', matcher.groups()[1]).split(',')
			element_list = [(variable_name, Operation.WRITE, indention, line) for variable_name in variables]
			# extract variables from expression
			element_list = self.parse_arithmetic_expression(element_list, matcher.groups()[2], indention, line_num, line)
			# add all variables into table
			self.variable_table[line_num] = element_list

			return True

		return False

	def is_print_statement(self, line_num, line, offset):
		# Extract variable from print statement
		matcher = re.match(r'([ \t]*)print[ \t]*\(?(.*)\)?([ \t]*#?.*)\n?$', line)
		if(matcher):
			indention = matcher.groups()[0].count('\t') + offset
			element_list = self.parse_arithmetic_expression([], re.sub(r'\)', '', matcher.groups()[1]), indention, line_num, line)
			# add all variables into table
			self.variable_table[line_num] = element_list
			return True

		return False

	def is_while_statement(self, line_num, line, offset):
		matcher = re.match(r'([ \t]*)while[ \t\(]*(.*)[\)]*:([ \t]*#?.*)\n$', line)
		if(matcher):
			indention = matcher.groups()[0].count('\t') + offset
			element_list = self.parse_boolean_expression([], re.sub(r'\)', '', matcher.groups()[1]), indention, line_num, line)
			# add all variables into table
			self.variable_table[line_num] = element_list
			return True

		return False

	def is_for_statement(self, line_num, line, offset):
		matcher = re.match(r'([ \t]*)for[ \t\(]*(.*)[ \t]*in[ \t]*(.*)[\)]*:([ \t]*#?.*)\n$', line)
		if(matcher):
			indention = matcher.groups()[0].count('\t') + 1 + offset
			# extract variable name
			variables = re.sub(r' ', '', matcher.groups()[1]).split(',')
			element_list = [(variable_name, Operation.ASSIGN, indention, line) for variable_name in variables]
			element_list = self.parse_function_expression(element_list, re.sub(r'\)', '', matcher.groups()[2]), indention, 
														  line_num, line)

			# add all variables into table
			self.variable_table[line_num] = element_list

			return True

		return False

	def is_if_statement(self, line_num, line, offset):
		# Extract variables from if statement
		matcher = re.match(r'([ \t]*)if[ \t\(]+(.*)\)?:([ \t]*#?.*)\n$', line)
		if(matcher):
			indention = matcher.groups()[0].count('\t') + offset
			element_list = self.parse_boolean_expression([], re.sub(r'\)', '', matcher.groups()[1]), indention, line_num, line)
			# add all variables into table
			self.variable_table[line_num] = element_list
			return True

		return False

	def is_with_statement(self, line_num, line, offset):
		matcher = re.match(r'([ \t]*)with[ \t]*(.*) as[ \t]*([A-Za-z0-9]+):([ \t]*#?.*)\n$', line)
		if(matcher):
			indention = matcher.groups()[0].count('\t')

			return True

		return False
			

	def parse_code(self, source_code_filepath):
		# parse the file
		with open(source_code_filepath, 'r') as fd:
			past_indention = 0
			indention = 0
			indention_offset = 0
			for line_num, line in enumerate(fd.readlines()):
				line_num += 1
				# Skip comments line or import line or empty line
				if(re.match(r'[ \t]*#.*$', line) or re.match(r'[ \t]*import.*$', line) or 
				   re.match(r'[ \t]*\n$', line) or re.match(r'if __name__ == "__main__":', line)
				  ):
					continue
				# Python scope can be determine by indention

				# pre-count indention
				matcher = re.match(r'([ \t]*).*$', line)
				indention = matcher.groups()[0].count('\t')

				if indention < past_indention and indention_offset < 0:
					indention_offset += 1


				if self.is_if_statement(line_num, line, indention_offset):
					indention_offset -= 1
				elif(self.is_function_def(line_num, line, indention_offset) or self.is_print_statement(line_num, line, indention_offset) or
				   self.is_for_statement(line_num, line, indention_offset) or self.is_while_statement(line_num, line, indention_offset) or
				   self.is_variable_assignment(line_num, line, indention_offset)
				  ):
					pass
				else:
					print("line: \"%s\" not supported"%repr(line))

				# pre-count tabs

				past_indention = indention

		# print(self.variable_table)








