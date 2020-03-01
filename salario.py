salarioAtual = int(input("Digite o Salario do Cliente: "))
#percentual de reajuste - 10porcento
reajuste = 110/100
novoSalario = salarioAtual * reajuste
print('O Salario era de: {}, \nAplicando reajuste: {}'.format(salarioAtual,novoSalario))