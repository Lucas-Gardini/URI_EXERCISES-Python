# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. 
# A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 
# 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

dinheiro = float(input())
restante = dinheiro
conversao = {
	'notas': {
		100: 0,
		50: 0,
		20: 0,
		10: 0,
		5: 0,
		2: 0,
	},
	'moedas': {
		1: 0,
		0.50: 0,
		0.25: 0,
		0.10: 0,
		0.05: 0,
		0.01: 0,
	}
}
cont = 0
while restante > 0:
	restante = float(f"{restante:.2f}")
	if restante >= 100:
		conversao['notas'][100] += 1
		restante -= 100
	elif restante >= 50:
		conversao['notas'][50] += 1
		restante -= 50
	elif restante >= 20:
		conversao['notas'][20] += 1
		restante -= 20
	elif restante >= 10:
		conversao['notas'][10] += 1
		restante -= 10
	elif restante >= 5:
		conversao['notas'][5] += 1
		restante -= 5
	elif restante >= 2:
		conversao['notas'][2] += 1
		restante -= 2
	elif restante >= 1:
		conversao['moedas'][1] += 1
		restante -= 1
	elif restante >= 0.50:
		conversao['moedas'][0.50] += 1
		restante -= 0.50
	elif restante >= 0.25:
		conversao['moedas'][0.25] += 1
		restante -= 0.25
	elif restante >= 0.10:
		conversao['moedas'][0.10] += 1
		restante -= 0.10
	elif restante >= 0.05:
		conversao['moedas'][0.05] += 1
		restante -= 0.05
	elif restante >= 0.01:
		conversao['moedas'][0.01] += 1
		restante -= 0.01

print(f"""NOTAS:
{conversao['notas'][100]} nota(s) de R$ 100.00
{conversao['notas'][50]} nota(s) de R$ 50.00
{conversao['notas'][20]} nota(s) de R$ 20.00
{conversao['notas'][10]} nota(s) de R$ 10.00
{conversao['notas'][5]} nota(s) de R$ 5.00
{conversao['notas'][2]} nota(s) de R$ 2.00
MOEDAS:
{conversao['moedas'][1]} moeda(s) de R$ 1.00
{conversao['moedas'][0.50]} moeda(s) de R$ 0.50
{conversao['moedas'][0.25]} moeda(s) de R$ 0.25
{conversao['moedas'][0.10]} moeda(s) de R$ 0.10
{conversao['moedas'][0.05]} moeda(s) de R$ 0.05
{conversao['moedas'][0.01]} moeda(s) de R$ 0.01""")