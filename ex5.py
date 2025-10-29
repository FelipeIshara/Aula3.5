usuarios = ["ana", "", "  ", "marcos", "chavosodausp123", "marcos@3"]

for usuario in usuarios:
    if not usuario:
        continue 
    for letra in usuario:
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
        print(f"Cadastrando usuário: {usuario}")
        continue
    
    print(f"Ignorando '{usuario}' (contém {validacao}).")