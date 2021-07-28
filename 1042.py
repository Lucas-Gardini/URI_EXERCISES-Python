# -*- coding: utf-8 -*-

numbers = [int(i) for i in input().split(" ")]
sorted = [*numbers]
sorted.sort()

for sortedNumber in sorted:
	print(sortedNumber)
print('')
for number in numbers:
	print(number)