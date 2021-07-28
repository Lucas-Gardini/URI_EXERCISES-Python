# -*- coding: utf-8 -*-

[x, y] = [float(i) for i in input().split(" ")]

def quadrante(x, y):
	if x == 0 and y == 0:
		print('Origem')
		return
	if x == 0:
		print ('Eixo Y')
		return
	if y == 0:
		print('Eixo X')
		return
	if x > 0 and y > 0:
		print('Q1')
	elif x > 0 and y < 0:
		print('Q4')
	elif x < 0 and y > 0:
		print('Q2')
	else:
		print('Q3')
		
quadrante(x, y)