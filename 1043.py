# -*- coding: utf-8 -*-

maybeTriangle = [float(i) for i in input().split()]
response = 0

if maybeTriangle[0] + maybeTriangle[1] > maybeTriangle[2] and maybeTriangle[0] + maybeTriangle[2] > maybeTriangle[1] and maybeTriangle[1] + maybeTriangle[2] > maybeTriangle[0]:
	response = maybeTriangle[0] + maybeTriangle[1] + maybeTriangle[2]
	print(f"Perimetro = {response}")
else:
	response = ((maybeTriangle[0] + maybeTriangle[1]) * maybeTriangle[2]) / 2
	print(f"Area = {response}")
