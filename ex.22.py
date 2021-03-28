n = str(input('escreva seu nome completo:')).strip()
s = n.upper()
p = n.lower()
print('seu nome em maiusculo é {} \n em minuculo é {}'.format(s, p))
print('e o total de letras é {}'.format(len(n) - n.count(' ')))
print('seu primeiro nome tem {} letras'.format(n.find(' ')))


