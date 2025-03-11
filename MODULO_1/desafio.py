contatos = []

def adicionar_contato():
  nome = input("Digite o nome do contato: ")
  telefone = input("Digite o telefone do contato: ")
  email = input("Digite o email do contato: ")
  favorito = False
  contato = {
    "nome": nome,
    "telefone": telefone,
    "email": email,
    "favorito": favorito
  }
  contatos.append(contato)
  print("Contato adicionado com sucesso!")
  return


def visualizar_lista_contatos():
  print("\nLista de contatos:", contatos)
  for indice, contato in enumerate(contatos, start=1):
    favorito = "⭐" if contato['favorito'] else " "
    print(f"{indice}. {contato['nome']} - {contato['telefone']} - {contato['email']} - Favorito: {favorito}")

def editar_contato():
  visualizar_lista_contatos()
  try:
    indice_contato = int(input("Digite o número do contato que deseja editar:")) - 1
    if 0 <= indice_contato < len(contatos):
      contatos[indice_contato]["nome"] = input("Digite o novo nome do contato: ")
      contatos[indice_contato]["telefone"] = input("Digite o novo telefone do contato: ")
      contatos[indice_contato]["email"] = input("Digite o novo email do contato: ")
      print("Contato editado com sucesso!")
    else:
      print("Contato não encontrado")
  except ValueError:
    print("Entrada inválida! Digite um número válido.\n")

def marcar_desmarcar_favorito():
  visualizar_lista_contatos()
  try:
    indice_contato = int(input("Digite o número do contato que deseja marcar/desmarcar como favorito:")) - 1
    if 0 <= indice_contato < len(contatos):
      contatos[indice_contato]["favorito"] = not contatos[indice_contato]["favorito"]
      estado = "marcado" if contatos[indice_contato]["favorito"] else "desmarcado"
      print(f"Contato {estado} como favorito!")
    else:
      print("Contato não encontrado")
  except ValueError:
    print("Entrada inválida! Digite um número válido.\n")

def visualizar_favoritos():
  favoritos = [contato for contato in contatos if contato["favorito"]]
  if not favoritos:
    print("\nNão há contatos favoritos")
    return
  print("\nLista de contatos favoritos:")
  for indice, contato in enumerate(favoritos, start=1):
    print(f"{indice}. {contato['nome']} - {contato['telefone']} - {contato['email']}")

def deletar_contato():
  visualizar_lista_contatos()
  try:
    indice_contato = int(input("Digite o número do contato que deseja deletar:")) - 1
    if 0 <= indice_contato < len(contatos):
      contatos.pop(indice_contato)
      print("Contato deletado com sucesso!")
    else:
      print("Contato não encontrado")
  except ValueError:
    print("Entrada inválida! Digite um número válido.\n")

while True:
  print("\nAgenda de contatos")
  print("1. Adicionar contato")
  print("2. Visualizar a lista de contatos")
  print("3. Editar um contato")
  print("4. Marcar/desmarcar um contato como favorito")
  print("5. Ver lista de contatos favoritos")
  print("6. Deletar um contato")
  print("7. Sair")

  escolha = input("Digite a sua escolha: ")
  if escolha == "1":
    adicionar_contato()
  elif escolha == "2":
    visualizar_lista_contatos()
  elif escolha == "3":
    editar_contato()
  elif escolha == "4":
    marcar_desmarcar_favorito()
  elif escolha == "5":
    visualizar_favoritos()
  elif escolha == "6":
    deletar_contato()
  elif escolha == "7":
    print("Até logo!")
    break
  