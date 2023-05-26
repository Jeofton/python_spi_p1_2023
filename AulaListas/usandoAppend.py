idades= []
maior = 0
cont = 0
for i in range(3):
    print("Digite a ",i+1,"ª idade:")
    idade = int(input())
    idades.append(idade)
print("Todas as idades digitadas")
print(idades)
for idade in idades:
    if idade > maior:
        maior = idade
print("*-*-*-*-*-*-*-*")
print("A maior idade digitada foi:", maior)