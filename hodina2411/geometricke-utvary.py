#program vykresluje geometricke tvary slozene ze znaku hezdicka

#funkce pro vykresleni ctverce
def ctverec(strana):
    radek = 0
    while radek < strana:
        print(strana * "*")
        radek += 1


print("kreslim geometricke tvary slozene ze znaku hezdicka")

pokracovat = True
while pokracovat:
    ctverec(5)
    odpoved = input("Chcete vykreslit dalsi geometricky tvar? (a/n) ").lower()
    if odpoved != "a":
        pokracovat = False

#funkce pro vykresleni obdelniku
def obdelnik(sirka, vyska):
    radek = 0
    while radek < vyska:
        print(sirka * "*")
        radek += 1

print("kreslim geometricke tvary slozene ze znaku hezdicka")

pokracovat = True
while pokracovat:
    obdelnik(3, 4)
    odpoved = input("Chcete vykreslit dalsi geometricky tvar? (a/n) ").lower()
    if odpoved != "a":
        pokracovat = False

 #funkce: nevyplneny obdelnik (a = sirka, b = vyska)

def nevyplneny_obdelnik(a, b):
    if a <= 0 or b <= 0:
        print("Delky stran musi byt kladne cislo.")
        return

    radek = 0
    while radek < b:
        if radek == 0 or radek == b - 1 or a == 1:
            print(a * "*")
        else:
            print("*" + (a - 2) * " " + "*")
        radek += 1
typ = input("jaky obrazec chces vykreslit?")
if typ == "c":
    ctverec(5)
elif typ == "o":
    obdelnik(3, 4)
elif typ == "on":
    nevyplneny_obdelnik(5, 4)
else:
    print("musis urcit jeden ze znamych tvaru! (c, o, on)")