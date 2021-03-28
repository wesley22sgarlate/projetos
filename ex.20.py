from random import shuffle
a1 = str(input('primeiro aluno:'))
a2 = str(input('segundo aluno:'))
a3 = str(input('terceiro aluno:'))
a4 = str(input('quarto aluno:'))
li = [a1, a2, a3, a4]
shuffle(li)
print('a ordem de apresentação é \n{}'.format(li))

