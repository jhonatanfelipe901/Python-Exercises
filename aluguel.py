kmPercorrido = int(input("Digite a Quantidade de Km Percorrido: "))
quantidadeDeDias = float(input("Digite a Quantidade de Dias que o carro rodou: "))
resul = (kmPercorrido * 0.15) + (quantidadeDeDias * 60)
print('O total a pagar é de R${:.2f}'.format(resul))
