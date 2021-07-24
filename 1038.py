# -*- coding: utf-8 -*-

produtos = {
	1: {'especificacao': 'Cachorro Quente', 'preco': 4.00},
	2: {'especificacao': 'X-Salada', 'preco': 4.50},
	3: {'especificacao': 'X-Bacon', 'preco': 5.00},
	4: {'especificacao': 'Torrada simples', 'preco': 2.00},
	5: {'especificacao': 'Refrigerante', 'preco': 1.50},
}

[codigo, quantidade] = input().split(" ")

print(f"Total: R$ {produtos[int(codigo)]['preco'] * int(quantidade):.2f}")