# Author: Hiu Hong Yu && Ming-Hung Lu
# University of California, Davis
# Winter 2017 - ECS 240 - Zhendong Su

#Standard Libraries

#3rd Party Libraries

#Local Libraries
import variable_table


class Undeclared_Local_Variable:

	def __init__(self):
		# __declared_var_list contains entries keyed by "level"
		#   each entry is a list of variable currently "declared" in that level
		self.__declared_var_list = {}

	def Check(self, var_table):
		warning_line_num = []
		line_num = 1;
		for code_line in var_table.variable_table:
			# get unique var-operation pair
			var_list = set(code_line)
			# sort the variable list so that read is processed before write
			var_list = sorted(var_list, key=lambda var: var[1])

			# clear all previous higher level variables
			for key, level in self.__declared_var_list.iteritems():
				if key > variable[2]:
					self.__declared_var_list[key] = []

			for variable in var_list:

				# if write operation, add var to declared list
				if variable[1] == variable_table.Operation.ASSIGN or variable[1] == variable_table.Operation.WRITE:
					# create container if not exist
					if not self.__declared_var_list.has_key(variable[2]):
						self.__declared_var_list[variable[2]] = []
					# prevent double adding of veriable to declared list
					if variable[0] not in self.__declared_var_list[variable[2]]:
						self.__declared_var_list[variable[2]].append(variable[0])
				else:
					found = False
					for i in range(0, variable[2] + 1):
						if self.__declared_var_list.has_key(i):
							if variable[0] in self.__declared_var_list[i]:
								found = True
					if not found:
						warning_line_num.append(line_num)

			line_num += 1
		return warning_line_num