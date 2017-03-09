# Author: Hiu Hong Yu && Ming-Hung Lu
# University of California, Davis
# Winter 2017 - ECS 240 - Zhendong Su

#Standard Libraries
import sys
import os

#3rd Party Libraries

#Local Libraries
import io_utils
import dirent_utils
import variable_table
import undeclared_local_variable_checker
import overriding_declared_variable_checker
import global_local_variable_confusion_checker
import function_parameter_overridden_checker

def perform_check(py_path):
	warning_lines = {}
	vtable = variable_table.Variable_Table(py_path)

	# I01
	ulv_instance = undeclared_local_variable.Undeclared_Local_Variable_Checker()
	warning_lines["Undeclared Local Variables"] = ulv_instance.check(vtable)

	# I02
	odv_instance = overriding_declared_variable.Overridding_Devlared_Variable_Checker()
	warning_lines["Overriding Declared Variables"] = odv_instance.check(vtable)

	# I03
	glvc_instance = global_local_variable_confusion.Global_Local_Variable_Confusion_Checker()
	warning_lines["Global/Local Variables Confusion"] = glvc_instance.check(vtable)

	# I04
	fpo_instance = function_parameter_overridden.Function_Parameter_Overridden_Checker()
	warning_lines["Function Parameter Overridden"] = fpo_instance.check(vtable)

	# return result
	return warning_lines


def main():
	# 
	if len(sys.argv) < 2:
		io_utils.usage("python main.py <source files>", terminate = True)

	# Make sure the input file is python
	if(dirent_utils.get_file_basename_extension(sys.argv[1])[1] != ".py"):
		io_utils.usage("python main.py <source file>", terminate = True)

	for py_path in sys.argv[1:]:
		print(perform_check(py_path))
	

if __name__ == "__main__":
	main()