# @classmethod
# @staticmethod

class MinhaClasse:
  valor = 10 # Atributo da classe
  def __init__(self, nome) -> None:
    self.nome = nome # Atributo da instância

  # requer uma instância para ser chamado
  def metodo_instancia(self):
    return f"Método de instância chamado para {self.valor}"
  
  @classmethod
  def metodo_classe(cls):
    return f"Método de classe chamado para valor = {cls.valor}"
  
  @staticmethod
  def metodo_estatico():
    return "Método estático chamado"
  

obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.metodo_instancia(obj)) # Passando a instância como argumento, isso não é possível de ser realizado
print(MinhaClasse.valor) # Acessando o atributo da classe, não precisa de uma instância
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
  def __init__(self, marca, modelo, ano) -> None:
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    
  @classmethod
  def criar_carro(cls, configuracao):
    marca, modelo, ano = configuracao.split(",")
    return cls(marca, modelo, int(ano))


configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print("Carro 1:", carro1.marca, carro1.modelo, carro1.ano)

class Matematica:
  
  @staticmethod
  def somar(a,b):
    return a + b
  
print(Matematica.somar(10, 15))