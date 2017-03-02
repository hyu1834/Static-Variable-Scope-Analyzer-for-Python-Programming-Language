import re

line = "\t\t\tif(index < argc):\n"
reg = re.compile(r'([ \t]*)if[ \t\(]*(.*)[\)]*:\n$')
matcher = re.match(reg, line)

if(matcher):
	print(matcher.groups())
	# print(line)