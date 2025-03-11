print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for elemento in lista:
  print(elemento)

print("For utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
  print(elemento)

pessoa = {"nome":"João", "idade": 30, "cidade": "São Paulo"}
print("For utilizando dicionário - chaves")

for chave in pessoa.keys():
  print(chave)

print("For utilizando dicionário - valores")
for valor in pessoa.values():
  print(valor)

for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")

# range(): intervalo numérico
# [0,1,2,3,4,5,6,7,8,9]
print("\n Utilizando a função range()")
print(list(range(0,10)))
for numero in range(5):
  print("Numero:", numero)

print("\n Utilizando a função range() com len()")
lista = [1,2,3,4,5]
print(lista)
for indice in range(0,len(lista)):
  if indice == 3:
    lista[indice] = 5
  else:
    lista[indice] = 0
  print(lista)

# enumarate()
lista_enumarate = ['a', 'b', 'c']
for letter in indice, valor in enumerate(lista_enumarate):
  print(f'{indice}: {valor}')
  if indice == 1:
    print("Indice 1")