# Declaração
nome_completo = "Gabriel Casemiro"

nome_completo_aspas = """Gabriel
Casemiro"""

nome_completo_quebra = "Gabriel \
  Casemiro"

nome = "Gabriel"
sobrenome = "Casemiro"

# Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma):" + nome_completo)
print("Nome completo (3a forma):" + "Gabriel" + " " + "Casemiro")
print("Nome completo (4a forma):" + "Gabriel", "Casemiro")
print("Nome completo (5a forma):", nome_completo_aspas)
print("Nome completo (6a forma):", nome_completo_quebra)
print("Nome completo (7a forma):%s" %nome_completo)
print("Nome completo (8a forma):%s %s" %(nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print('Nome completo (10a forma): {} {}'.format(nome, sobrenome))

print(nome.lower())
print(nome.upper())

print(nome_completo.count('a'))
print(nome_completo.find('a'))

print(nome.encode())
print(nome.encode().decode())

print(nome_completo.replace('b', 'a'))
print(nome_completo.replace('a', '123'))

telefone = '(19)97325-0502'
print(telefone.replace('(', ''))
print(telefone.replace("(", "").replace(")", "").replace("-", ""))
print(telefone.replace("a", "123"))

print('-'.join('Gabriel'))

print(nome_completo.split(' '))
print(nome_completo.split())

nome = 'xGabriel Casemirox'
print(nome.strip('x'))
print(nome.strip('a'))
print(nome.rstrip('x'))

print(nome_completo.startswith('Ga'))
print(nome_completo.startswith('Be'))

print('el' in nome_completo)
print('abc' not in nome_completo)