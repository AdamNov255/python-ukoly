import random
tajne_cislo = random.randint (1,20)
pocitadlo = 0
tip = 0
max_pokusy = 5


while tip != tajne_cislo and pocitadlo < max_pokusy:
    tip = int(input("Tipni si cislo od 1 do 20: "))
    pocitadlo += 1
    if tip < tajne_cislo:
        print("Tvoje cislo je mensi nez tajne cislo")
    elif tip > tajne_cislo:
        print("Tvoje cislo je vetsi nez tajne cislo")
    else:
        print("Uhadl jsi! Tajne cislo bylo:", tajne_cislo)
        print("Pocet pokusu:", pocitadlo)
else:
    if tip != tajne_cislo:
        print("Neuhadl jsi! Tajne cislo bylo:", tajne_cislo)
        print("Pocet pokusu:", pocitadlo)