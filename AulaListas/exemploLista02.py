idades = [int(input("Digite a sua idade: ")),
          int(input("Digite a sua idade: ")),
          int(input("Digite a sua idade: "))
         ]
maior = 0;

for idade in idades:
    if idade > maior:
        maior = idade;

print("A maior idade digitada foi: ",maior)