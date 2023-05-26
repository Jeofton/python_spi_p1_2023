lista_de_exemplos = ['Carolina', 'Jussier', 'Evellyn']
print("Lista original:\n", lista_de_exemplos)
print(' ')

lista_de_exemplos[1]= 'Ivanise'

print('Lista com a alteração do valor do elemento no índice 1:\n', lista_de_exemplos)
print(' ')

lista_de_exemplos.insert(2, "Gabrielle")
print('Lista com a inserção de elemento no índice 2, com o método insert():\n', lista_de_exemplos)
print(' ')

del lista_de_exemplos[0]
print('Lista com a exclusão do elemento no índice 0:\n', lista_de_exemplos)
print(' ')

lista_de_exemplos.append('Carolina')
print('Lista com a adição de elemento com método append:\n', lista_de_exemplos)
print(' ')

lista_de_exemplos.append('Najla')
print('Lista com a adição de elemento com método append():\n', lista_de_exemplos)
print(' ')

lista_de_exemplos.pop()
print('Lista com a remoção de elemento com método pop():\n', lista_de_exemplos)
print(' ')

lista_de_exemplos.insert(1, "Najla")
print('Lista com a inserção de elemento no índice 1, com o método insert():\n', lista_de_exemplos)
print(' ')

lista_de_exemplos.pop(1)
print('Lista com a extração de elemento de índice 1 passando o método pop() com parâmetro:\n', lista_de_exemplos)
print(' ')

lista_de_exemplos.insert(3, "Najla")
print('Lista com a inserção de elemento no índice 3, com o método insert():\n', lista_de_exemplos)
print(' ')

lista_de_exemplos.remove("Najla")
print('Lista com a remoção de elemento pelo valor:\n', lista_de_exemplos)
print(' ')

lista_de_exemplos.sort()
print('Lista ordenada alfabeticamente:\n', lista_de_exemplos)
print(' ')

lista_de_exemplos.sort(reverse=True)
print('Lista ordenada alfabeticamente ordem inversa:\n', lista_de_exemplos)
print(' ')


print('Lista ordenação temporária:\n', sorted(lista_de_exemplos))
print('Lista original:\n', lista_de_exemplos)
lista_de_exemplos.sort()
print('Lista ordenada alfabeticamente:\n', lista_de_exemplos)
print('Lista reversa:\n', sorted(lista_de_exemplos, reverse=True))
print(' ')

lista_de_exemplos.sort()
print('Lista ordenada alfabeticamente:\n', lista_de_exemplos)
print(' ')

lista_de_exemplos.reverse()
print('Lista revertida:\n',lista_de_exemplos)
print(' ')

print('Tamanho da lista:\n', len(lista_de_exemplos))
print(' ')

