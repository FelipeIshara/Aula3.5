#for loop em list

#passo1 - for loop simples em list
# moradores = ["Chaves", "Kiko", "Chiquinha"]
# for morador in moradores:
#     print(morador)

#passo2 - for loop aninhado
moradores = ["Chaves", "Kiko", "Chiquinha"]
for morador in moradores:
    for letra in morador:
        print(letra)
    print()
        