salario = float(input("Informe seu salario:"))
"""novosalario = 0.0"""
if salario < 500.00:
    salario = salario * 1.5
    print("Seu novo salário é: ",salario,"\n")
elif salario >= 500.00 and salario <= 750.00:
    salario = salario * 1.25
    print("Seu novo salário é: ",salario,"\n")
else:
    salario = salario * 1.15
    print("Seu novo salário é: ",salario,"\n")
print("Fim dos cálculos.")
