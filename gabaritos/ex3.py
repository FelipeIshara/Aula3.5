
# inventario = ["elmo", "", "capacete", "botas"]
# for item in inventario:
#     if item == "espada":
#         print(" Espada encontrada")
#         break
# else:
#     print("Espada não encontrada.")


# inventario = ["elmo", "espada", "capacete", "botas"]
# busca = "espada"
# for item in inventario:
#     if item == busca:
#         print(f"{item.capitalize()} encontrado(a)")
#         break
# else:
#     print(f"{busca.capitalize()} não está no inventário.")

inventario = ["elmo", "espada", "capacete", "botas"]
busca = input("informe um item: ")
for item in inventario:
    if item == busca:
        print(f"{item.capitalize()} encontrado(a)")
        break
else:
    print(f"{busca.capitalize()} não está no inventário.")

# inventario = ["elmo", "espada", "capacete", "botas"]
# busca = "espada"

# if busca in inventario:
#     print(f"{busca.capitalize()} encontrado(a).")
# else:
#     print(f"{busca.capitalize()} não está no inventário.")