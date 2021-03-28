from math import hypot
h = float(input('quanto mede o cateto oposto?'))
b = float(input('quanto mede o cateto adejasente?'))
s = hypot(b, h)
print('logo sua hipotenusa é de {:.2f}'.format(s))

