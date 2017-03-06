import re

line = "for i in range(1, 10):\n"
reg = re.compile(r'([ \t]*)for[ \t\(]*(.*)[ \t]*in[ \t]*(.*)[\)]*:\n$')
matcher = re.match(reg, line)

if(matcher):
	print(matcher.groups())
	# print(line)