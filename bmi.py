print('請輸入你要的功能')
print('	1. 計算BMI')
print('	2. 用身高計算適合體重')
choose_function = input('數字選項')

if choose_function == '1':
	height = input('請輸入身高: ')
	weight = input('請輸入體重: ')
	weight = float(weight)
	height = float(height) / 100
	#上面為輸入身高體重
	bmi = weight / (height * height)
	#	print(bmi) #算出BMI
	if bmi < 18.5:
		print('你體重過輕啦~')
	elif bmi >= 18.5 and bmi < 24:
		print('你身材剛好喔~')
	elif bmi >= 24 and bmi <27:
		print('已經過重了呢!!')
	elif bmi >= 27 and bmi < 30:
		print('已經輕度肥胖囉!!!!')
	elif bmi >=30 and bmi <35:
		print('這個是中度肥胖喔...')
	else:
		print('你這個是重度肥胖了，減減肥吧@@')
elif choose_function == 2:
	height = input('請輸入身高: ')
	weight = input('請輸入體重: ')
	weight = float(weight)
	height = float(height) / 100
	bmi = weight / (height * height)
	weight_min = 18.5 * height * height
	weight_max = 24 * height * height
	height = height * 100
	if bmi < 18.5:
		height_min = ((weight_min / bmi) ** 0.5) * 100
		print(height, height_min)
		print('你適合的體重介於', weight_min, '~', weight_max,'之間喔')
		print('不然你就要把你的身高降低', abs(height - height_min))
	elif bmi > 24:
		height_max = ((weight_max / bmi) ** 0.5) * 100
		print('你適合的體重介於', weight_min, '~', weight_max,'之間喔')
		print('不然你就要把你的身高增加', abs(height_max - height))
	else:
		print('你適合的體重介於', weight_min, '~', weight_max,'之間喔')
		print('你剛好了~~讚讚讚!!!')
else:
	print('只能選1或2啦!!!')
	

