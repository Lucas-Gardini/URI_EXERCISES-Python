#  -*- coding: utf-8 -*-

# Resposta correta mas não aceita

c = int(input())
respostas = []
for i in range(0, c):
	n = str(input()).split(" ")
	nRange = n[0]
	if int(nRange) >= 1 and int(nRange) <= 1000:
		n.pop(0)
		mediaTurma = 0
		mediaAlunos = 0
		podeContinuar = True
		for ii in n:
			if (int(ii) >= 0 and int(ii) <= 100):
				mediaTurma += int(ii)
			else:
				podeContinuar = False
		if (podeContinuar):
			mediaTurma = mediaTurma / int(nRange)
			for iii in n:
				if int(iii) > mediaTurma:
					mediaAlunos += 1
			mediaAlunos = (mediaAlunos * 100) / int(nRange)
			respostas.append(f"{mediaAlunos:.3f}%")
for resposta in respostas:
	print(resposta)