#this is a test file

import os
import sys

def test1(arg1, arg2, arg3):
	i = 10
	for i in range(1, 10):
		i = i + 1 + i + i

	print i + 1
	if(i == 1):
		print(i)