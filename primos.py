num = int(input("Digite um numero: "))
tot = 0; #essa variavel e pra eu saber o numero de divisiveis
for c in range(1, num + 1):
  #se o num for divisivel por algum numero do contador(c)
  if num % c == 0:
    print('\033[33m', end='')
    tot += 1
    #SE O NUMERO FOI DIVISIVEL, E MAIS UM NUMERO NO TOTAL
  else:
    print('\033[31m', end='')
  print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
  print("E por isso ele é PRIMO")
else:
  print("e por isso ele nao é PRIMO")