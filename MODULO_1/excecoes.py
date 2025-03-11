print("Exemplo de captura de exceções")
try:
  numero = int(input("Digite um número inteiro: "))
  resultado = 10 / numero
  print("O resultado da divisão é: ", resultado)
except ValueError as e:
  print(f"Erro de value error: {e}")
  raise ValueError("Tipo de variáveis incompatíveis")
except Exception as e:
  print(f"Erro: {e}")
else:
  print(f"Resultado: {resultado}")
finally:
  print("Operação finalizada.")