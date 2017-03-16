# Author: Hiu Hong Yu && Ming-Hung Lu
# University of California, Davis
# Winter 2017 - ECS 240 - Zhendong Su

#Standard Libraries

#3rd Party Libraries

#Local Libraries
import variable_table


class Overridding_Declared_Variable_Checker:
	def __init__(self):
		# __declared_var_list contains entries keyed by "level"
		#   each entry is a list of variable currently "declared" in that level
		self.__declared_var_list = []

	def check(self, vtable):
		warning_line_num = []
		# for every line
		for line_num, code_line in vtable.variable_table.items():
			# get unique var-operation pair
			var_list = set(code_line)

			# for every cariable in such line
			for variable in var_list:
				# if variable is write or arg
				if any(variable[1] == operation for operation in [variable_table.Operation.WRITE,
																  variable_table.Operation.ARG
																 ]):
					# if this is the first time seeing this variable
					# add it into the list
					if not variable[0] in self.__declared_var_list:
						self.__declared_var_list.append(variable[0])
				# if it is assignment operation
				if variable[1] == variable_table.Operation.ASSIGN:
					for variable_name in self.__declared_var_list:
						if variable[0] == variable_name:
							warning_line_num.append("%s: %s"%(line_num, variable[3]))
				# we do not care about read in this checker
					

		return warning_line_num