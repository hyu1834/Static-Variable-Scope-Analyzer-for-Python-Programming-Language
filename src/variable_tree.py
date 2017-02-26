# Author: Hiu Hong Yu && Ming-Hung Lu
# University of California, Davis
# Winter 2017 - ECS 240 - Zhendong Su

#Standard Libraries

#3rd Party Libraries

#Local Libraries
import undeclared_local_variable
import overriding_declared_variable
import global_local_variable_confusion


class Variable_Tree:
	def __init__(self):
		variable_tree = []

	def parse_code(self, source_code_filepath):
		# parse the file
		with open(source_code_filepath, 'r') as fd:
			for line in fd.readlines():
				print(line)