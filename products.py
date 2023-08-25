Pro = []

with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue 
		name, price = line.strip().split(',')
		Pro.append([name, price])
print(Pro)


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