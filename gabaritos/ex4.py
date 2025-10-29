usuarios = ["ana", "", "felipe_ishara", "  ", "marcos", "chavosodausp123", "marcos@3"]

# passo1 - cadastrar qualquer usuario
for usuario in usuarios: 
    print(f"Cadastrando usuário: {usuario.capitalize()}")

# passo2 - cadastrar somente se a string não for vazia
for usuario in usuarios:
    if usuario:  
        print(f"Cadastrando usuário: {usuario.capitalize()}")