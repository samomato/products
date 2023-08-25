import os #operating system 因為單單程式沒有權限去檢查檔案
Pro = []
if os.path.isfile('products.py'):  #檢查檔案在否
	print("Yeah! 找到檔案了")
	with open('products.csv', 'r', encoding = 'utf-8') as f: 
	for line in f:
		if '商品,價格' in line:
			continue 
		name, price = line.strip().split(',')
		Pro.append([name, price])
	print(Pro)

else:
	print("找不到檔案R")

# 在原有檔案內容的基礎下，加上以下新的資料

while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	Pro.append([name, price])
print(Pro)

# 以下寫入檔案
with open('products.csv', 'w', encoding='utf-8') as pf:
	pf.write('商品,價格\n')
	for p in Pro:
		pf.write(p[0] + ',' + str(p[1]) + '\n')

#最後再寫入檔案