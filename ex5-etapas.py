usuarios = ["ana", "", "  ", "marcos", "chavosodausp123", "marcos@3"]

#passo1 - validar espaço vazio
for usuarios in usuarios:
    if not usuarios:
        continue 

    for letra in usuarios:
        if letra.isspace():
            print(f"Ignorando '{usuarios}', (contém espaços vazios).")
            break
    else:
        print(f"Cadastrando usuário: {usuarios}")

#passo2 - adicionar outras validações
for usuarios in usuarios:
    if not usuarios:
        continue 

    for letra in usuarios:
        if letra.isspace():
            print(f"Ignorando '{usuarios}', (contém espaços vazios).")
            break
        if letra.isalpha():
            print(f"Ignorando '{usuarios}', (contém caractéres especiais).")
            break
    else:
        print(f"Cadastrando usuário: {usuarios)}")

#passo3 - refatorar para evitar multiplos prints, uso do  else nos loops
for usuarios in usuarios:
    if not usuarios:
        continue 

    for letra in usuarios:
        if letra.isdigit():
            validacao = "números"
            break
        elif letra.isspace():
            validacao = "espaços vazios"
            break
        elif not letra.isalpha():
            validacao = "caracteres especiais"
            break
    else:
        print(f"Cadastrando usuário: {usuarios}")
        continue
    
    print(f"Ignorando '{usuarios}' (contém {validacao}).")
