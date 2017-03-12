# Author: Hiu Hong Yu && Ming-Hung Lu
# University of California, Davis
# Winter 2017 - ECS 240 - Zhendong Su

#Standard Libraries

#3rd Party Libraries

#Local Libraries
import variable_table


class Function_Parameter_Overridden_Checker:
	def __init__(self):
		# __declared_var_list contains entries keyed by "level"
		#   each entry is a list of variable currently "declared" in that level
		self.__declared_var_list = {}

	def check(self, vtable):
		warning_line_num = []
		# for every line
		for line_num, code_line in vtable.variable_table.items():
			# get unique var-operation pair
			var_list = set(code_line)

			# for every cariable in such line
			for variable in var_list:
				# build table for with function argurment only
				if variable[1] == variable_table.Operation.ARG:
					# if this is the first time c this indention
					if not variable[2] in self.__declared_var_list.keys():
						self.__declared_var_list[variable[2]] = [variable[0]]
					elif not variable[0] in self.__declared_var_list[variable[2]]:
						self.__declared_var_list[variable[2]].append(variable[0])


				# we only care about write or assign operation
				if any(variable[1] == operation for operation in [variable_table.Operation.WRITE,
																  variable_table.Operation.ASSIGN
																 ]):
					pass

		return warning_line_num


		