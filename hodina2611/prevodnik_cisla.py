def cifra_na_znak(hodnota):
    if hodnota < 10:
        return str(hodnota)
    elif hodnota == 10:
        return "A"
    elif hodnota == 11:
        return "B"
    elif hodnota == 12:
        return "C"
    elif hodnota == 13:
        return "D"  
    elif hodnota == 14:
        return "E"
    else:
        return "F"

def prevod_soustavu(cislo, zaklad):
    if cislo < 0:
        return None
    if zaklad != 2 and zaklad != 8 and zaklad != 16:
        return None
    if cislo == 0:
        return "0"

    vysledek = ""
    while cislo > 0:
        zbytek = cislo % zaklad
        vysledek = cifra_na_znak(zbytek) + vysledek
        cislo //= zaklad

    return vysledek

print("DEC | BIN | OCT | HEX")
print("-------------------")

i = 0
while i <= 16:
    bin_val = prevod_soustavu(i, 2)
    oct_val = prevod_soustavu(i, 8)
    hex_val = prevod_soustavu(i, 16)
    print(f"{i:<3} | {bin_val:<5} | {oct_val:<3} | {hex_val:<3}")
    i = i + 1

print("-"*36)

print("Test neplatného čísla:", prevod_soustavu(-3, 2))
print("Test neplatného základu:", prevod_soustavu(10, 5))