inventario = ["elmo", "espada", "capacete", "botas"]
busca = "espada"
for item in inventario:
    if item == busca:
        print(f"{item.capitalize()} encontrado(a)")
        break
else:
    print(f"{busca.capitalize()} não está no inventário.")