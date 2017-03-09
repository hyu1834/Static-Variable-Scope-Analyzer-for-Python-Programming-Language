# Author: Hiu Hong Yu && Ming-Hung Lu
# University of California, Davis
# Winter 2017 - ECS 240 - Zhendong Su

#Standard Libraries

#3rd Party Libraries

#Local Libraries
import variable_table


class Global_Local_Variable_Confusion_Checker:
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
				# we only care about write or assign operation
				if variable[1] == variable_table.Operation.WRITE or variable[1] == variable_table.Operation.ASSIGN:
					# if the indention is 0 = global variable
					if variable[2] == 0 and not variable[0] in self.__declared_var_list:
						# add it to the list
						self.__declared_var_list.append(variable[0])
					elif variable[2] > 0 and variable[0] in self.__declared_var_list:
						warning_line_num.append("%s: %s"%(line_num, variable[3]))

		return warning_line_num

