usuarios = ["ana", "", "felipe_ishara", "  ", "marcos", "chavosodausp123", "marcos@3"]

passo1 - cadastrar qualquer nome
for nome in usuarios: 
    print(f"Cadastrando usuário: {nome.capitalize()}")

passo2 - cadastrar somente se a string não for vazia
for nome in usuarios:
    if nome:  
        print(f"Cadastrando usuário: {nome.capitalize()}")