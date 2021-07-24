intervalo = float(input())
if intervalo >=0 and intervalo <= 25:
	print("Intervalo [0,25]")
elif intervalo > 25 and intervalo <= 50:
	print("Intervalo (25,50]")
elif intervalo > 50 and intervalo <= 75:
	print("Intervalo (50,75]")
elif intervalo > 75 and intervalo <= 100:
	print("Intervalo (75,100]")
else:
	print("Fora de intervalo")