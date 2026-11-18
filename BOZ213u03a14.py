liste = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]

yeni_liste = []

for sayi in liste:
    if sayi not in yeni_liste:
        yeni_liste.append(sayi)

print("Tekrarsız liste:", yeni_liste)
