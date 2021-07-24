[A, B, C] = [float(i) for i in input().split(" ")]

try:
	delta = B**2 - 4 * A * C
	x1 = (-B + delta**(1/2))/(2 * A)
	x2 = (-B - delta**(1/2))/(2 * A)
	if delta >= 0:
		print(f"R1 = {x1:.5f}")
		print(f"R2 = {x2:.5f}")
	else:
		print('Impossivel calcular')
except:
	print('Impossivel calcular')

