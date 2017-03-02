# Author: Hiu Hong Yu && Ming-Hung Lu
# University of California, Davis
# Winter 2017 - ECS 240 - Zhendong Su

#Standard Libraries
import re

#3rd Party Libraries

#Local Libraries
import undeclared_local_variable
import overriding_declared_variable
import global_local_variable_confusion
import function_parameter_overridden


class Variable_Table:
	def __init__(self, source_code_filepath):
		# Dict for variable table
		self.variable_table = {}
		self.parse_code(source_code_filepath)

	def parse_code(self, source_code_filepath):
		# parse the file
		with open(source_code_filepath, 'r') as fd:
			indention = 0
			for line in fd.readlines():
				# Skip comments line or import line or empty line
				if(re.match(r'[ \t]*#.*$', line) or re.match(r'[ \t]*import.*$', line) or 
				   re.match(r'[ \t]*\n$', line) or re.match(r'if __name__ == "__main__":', line)
				  ):
					continue
				# Python scope can be determine by indention
				# if it is a function defination
				matcher = re.match(r'[ \t]*def ([A-Za-z0-9]+)(\(([A-Za-z0-9]*(,[ \t]*[A-Za-z0-9]+)*)\)):\n$', line)
				if(matcher):
					function_name = matcher.groups()[0]
					function_args = re.sub(r' ', '', str(matcher.groups()[2])).split(',') if(matcher.groups()[2]) else []
					print("def", function_name, function_args)
					continue
				
				# Variable assignment
				matcher = re.match(r'([ \t]*)(.*)[ \t]*=[ \t]*(.*)\n$', line)
				if(matcher):
					indention = matcher.groups()[0].count('\t')
					result_variables = re.sub(r' ', '', matcher.groups()[1]).split(',')
					expression = matcher.groups()[2]
					print("Assign", indention, result_variables, expression)
					continue

				# While loop
				matcher = re.match(r'([ \t]*)while[ \t\()]*(.*)[\)]*:\n$', line)
				if(matcher):
					indention = matcher.groups()[0].count('\t')
					expression = matcher.groups()[1]
					print("while", indention, expression)
					continue

				# For loop
				matcher = re.match(r'([ \t]*)for[ \t\(]*([_A-Za-z0-9]+)[ \t]*in[ \t]*(.*)[\)]*:\n$', line)
				if(matcher):
					indention = matcher.groups()[0].count('\t')
					expression = re.sub(r'\)', '', matcher.groups()[1])
					print("for", indention, expression)
					continue

				# If
				matcher = re.match(r'([ \t]*)if[ \t\(]*(.*)[\)]*:\n$', line)
				if(matcher):
					indention = matcher.groups()[0].count('\t')
					expression = re.sub(r'\)', '', matcher.groups()[1])
					print("if", indention, expression)
					continue

				# With Statement
				matcher = re.match(r'([ \t]*)with[ \t]*(.*) as[ \t]*([A-Za-z0-9]+):\n$', line)
				if(matcher):
					indention = matcher.groups()[0].count('\t')
					expression = matcher.groups()[1]
					variable_name = matcher.groups()[2]
					print("with",indention, expression, variable_name)
					continue

				print(repr(line))








