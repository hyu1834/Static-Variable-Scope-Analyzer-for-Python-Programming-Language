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
import undeclared_local_variable


def main():
	# 
	if len(sys.argv) < 2:
		io_utils.usage("python main.py <source file>", terminate = True)

	# Make sure the input file is python
	if(dirent_utils.get_file_basename_extension(sys.argv[1])[1] != ".py"):
		io_utils.usage("python main.py <source file>", terminate = True)

	vtable = variable_table.Variable_Table(sys.argv[1])

	# checking I01
	ULVList = undeclared_local_variable.Undeclared_Local_Variable()
	print ULVList.Check(vtable)


if __name__ == "__main__":
	main()