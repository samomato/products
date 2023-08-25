import os #operating system 因為單單程式沒有權限去檢查檔案

def read_file(filename):
	Pro = []
	with open(filename, 'r', encoding = 'utf-8') as f: 
		for line in f:
			if '商品,價格' in line:
				continue 
			name, price = line.strip().split(',')
			Pro.append([name, price])
	return Pro
	

# 在原有檔案內容的基礎下，加上以下新的資料
def user_input(Pro):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		price = int(price)
		Pro.append([name, price])
	print(Pro)
	return Pro

#最後再寫入檔案
def write_file(filename, Pro):
	with open(filename, 'w', encoding='utf-8') as pf:
		pf.write('商品,價格\n')
		for p in Pro:
			pf.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):  #檢查檔案在否
		print("Yeah! 找到檔案了")
		products = read_file(filename)
	else:
		print("找不到檔案R")

	products = user_input(products)
	write_file(filename, products)

main()