# -*- coding: utf-8 -*-

numbers = [int(i) for i in input().split()]
if numbers[0] % numbers[1] == 0:
	print('Sao Multiplos')
elif numbers[1] % numbers[0] == 0:
	print('Sao Multiplos')
else:
	print('Nao sao Multiplos')