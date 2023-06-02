from funcoes import *
def verificaAprovacao(n1, n2, n3):
    s1 = soma(n1,n2,n3)
    # s2 = soma(n3,s1)
    media = calculaMedia(s1)

    if media >= 7:
        print("O aluno está aprovado")
    else:
        print("O aluno está reprovado")

