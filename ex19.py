import random
n1 = str(input('digite um nome:'))
n2 = str(input('digite outro:'))
n3 = str(input('digite outro:'))
n4 = str(input('digite outro:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('o escolhido é {}'.format(escolhido) )

