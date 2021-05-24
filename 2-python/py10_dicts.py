lista_craques = ["Gabriel", "Giorgian", "Diego"]

dict_craques = {"Gabriel": "Atacante", "Giorgian": "Meia", "Diego": "Goleiro"}

#print(dict_craques["Gabriel"])

time = {
    "Goleiro": "Diego",
    "Zagueiros": ["Fulano", "Beltrano"],
    "Meias": ["Giorgian", "Gerson"],
    "Atacantes": ["Gabi", "Bruno", "Pedro"]
}

print(time["Meias"])

for jogador in time["Atacantes"]:
  print(jogador)