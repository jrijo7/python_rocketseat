# Exemplo
def saudacao(nome):
  print(f"Olá, {nome}!")

print("\n Chamando a função saudacao:")
saudacao("Alice")
saudacao("Bob")

# Funcao com retorno
def quadrado(numero):
  resultado = numero ** 2
  return resultado

print("\nChamando função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da funcao quadrado: ", resultado_quadrado)

# Funcao com multiplos parametros
def soma(numero1, numero2):
  resultado = numero1 + numero2
  return resultado

print("\nChamando a função soma:")
resultado_soma = soma(numero1,numero2)
print("A soma do número %s e número %s é %s" % (numero1, numero2, resultado_soma))