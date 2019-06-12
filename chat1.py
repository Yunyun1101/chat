#讀檔案
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			chat.append(line.strip())
	return chat

#處理檔案, 回傳讀取陣列
def convert(lines):
	#n[0:3] (開始值有含, 結束值不包含, 若開始值是0, 則可以省略)
	#n[-2:] (可以從結尾開始拿倒數兩個)
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0	

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1			
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen 貼圖:', allen_sticker_count)
	print('Allen 圖片:', allen_image_count)
	print('Allen word count:', allen_word_count)
	print('Viki 貼圖:', viki_sticker_count)
	print('Viki 圖片:', viki_image_count)
	print('Viki word count:', viki_word_count)

	#return new

#寫入檔案
def write_file(statements, filename):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for statement in statements:
			f.write(statement + '\n')

def main():
	lines = read_file('-LINE-Viki.txt')
	convert(lines)
	#write_file(statements, 'output.txt')

main()