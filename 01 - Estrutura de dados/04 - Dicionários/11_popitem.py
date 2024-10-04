contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}, "br.serafim@gmal.com": {"nome": "Bruno", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(contatos)

resultado2 = resultado.popitem()
print(resultado2)