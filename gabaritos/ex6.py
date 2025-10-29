def main():
    usuarios = ["ana", "", "  ", "marcos", "chavosodausp123", "marcos@3"]
    for usuario in usuarios:
        ok, motivo = validar_nome(usuario)
        if ok:
            print(f"Cadastrando usuário: {usuario.capitalize()}")
        else:
            print(f"Ignorando '{usuario}' (contém {motivo}).")

def validar_nome(usuario: str):
    if not usuario:
        return False, "vazio"
    for ch in usuario:
        if ch.isdigit():
            return False, "números"
        if ch.isspace():
            return False, "espaços vazios"
        if not ch.isalpha():
            return False, "caracteres especiais"
    return True, None

main()
