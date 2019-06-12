lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip()) #strip 去除空行

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	print('time:', time)
	name = s[0][5:]
	print('name:', name)