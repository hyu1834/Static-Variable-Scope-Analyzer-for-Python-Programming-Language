# Author: Hiu Hong Yu && Ming-Hung Lu
# University of California, Davis
# Winter 2017 - ECS 240 - Zhendong Su

#Standard Libraries
import sys
import os

#3rd Party Libraries

#Local Libraries
import io_utils.py
import dirent_utils
import variable_tree


def main():
	# 
	if len(sys.argv) < 2:
		io_utils.usage("python main.py <source file>", terminate = True)

	# Make sure the input file is python
	if(dirent_utils.get_file_basename_extension(sys.argv[1])[1] != ".py"):
		io_utils.usage("python main.py <source file>", terminate = True)

	tree = variable_tree.Variable_Tree(sys.argv[1])


if __name__ == "__main__":
	main()