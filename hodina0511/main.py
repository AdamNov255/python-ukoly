print("mysli si cislo od 1 do 100")
print("odpovidej pouze: v (vetsi), m (mensi), s (spravne),")
print("-" * 40)

dole = 1
nahore = 100
pokusy = 0
odpoved = ""

# cyklus pobezi, dokud odpoved nebude "s" (spravne)
while odpoved != "s":

    # vypocet stredu intervalu
    tip = (dole + nahore) // 2

    # zobrazeni tipu a ziskani odpovedi od uzivatele
    print("muj tip:", tip)
    odpoved = input("zadej odpoved (v / m / s): ")

    # uprava hranic podle odpovedi
    if odpoved == "v":
        dole = tip + 1
    elif odpoved == "m":
        nahore = tip - 1
    elif odpoved == "s":
        print("suepr, mam to")
        print("pocet pokusu:", pokusy)
    else:
        print("neznama odpoved, zadej prosim 'v', 'm' nebo 's'. ")
        pokusy = pokusy - 1 #nepltany pokus se nepocita
        