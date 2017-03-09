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

def perform_check(py_path, ulv_checker, odv_checker, glvc_checker, fpo_checker):
	warning_lines = {}
	vtable = variable_table.Variable_Table(py_path)

	# I01
	warning_lines["Undeclared Local Variables"] = ulv_checker.check(vtable)

	# I02
	warning_lines["Overriding Declared Variables"] = odv_checker.check(vtable)

	# I03
	warning_lines["Global/Local Variables Confusion"] = glvc_checker.check(vtable)

	# I04
	warning_lines["Function Parameter Overridden"] = fpo_checker.check(vtable)

	# return result
	return warning_lines


def main():
	# 
	if len(sys.argv) < 2:
		io_utils.usage("python main.py <source files>", terminate = True)

	# Make sure the input file is python
	if(dirent_utils.get_file_basename_extension(sys.argv[1])[1] != ".py"):
		io_utils.usage("python main.py <source file>", terminate = True)


	# Init checker
	ulv_checker = undeclared_local_variable_checker.Undeclared_Local_Variable_Checker()
	odv_checker = overriding_declared_variable_checker.Overridding_Devlared_Variable_Checker()
	glvc_checker = global_local_variable_confusion_checker.Global_Local_Variable_Confusion_Checker()
	fpo_checker = function_parameter_overridden_checker.Function_Parameter_Overridden_Checker()

	# Perform analysis on each python file
	for py_path in sys.argv[1:]:
		print(perform_check(py_path, ulv_checker, odv_checker, glvc_checker, fpo_checker))
	

if __name__ == "__main__":
	main()