#讀檔案
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			chat.append(line.strip())
	return chat

#處理檔案, 回傳讀取陣列
def convert(lines):
	name = None #其他語言是null
	statements = []
	for line in lines:
		if 'Allen' in line:
			name = 'Allen'
			continue
		elif line == 'Tom':
			name = 'Tom'
			continue
		else:
			statements.append(name + ':' + line)
	return statements

#寫入檔案
def write_file(statements, filename):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for statement in statements:
			f.write(statement + '\n')

def main():
	lines = read_file('input.txt')
	statements = convert(lines)
	write_file(statements, 'output.txt')

main()