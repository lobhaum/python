idade = int(input('Digita a idade: '))
maior_idade = idade > 18
crianca = idade < 12
adolescente = idade > 12
bool_maior = bool(maior_idade)
bool_crianca = bool(crianca)
bool_adolescente = bool(adolescente)
print(f'maior:{bool_maior}')
print(f'crianca: {bool_crianca}')
print(f'adolescente: {bool_adolescente}')
