#********************
# kalkulacka spropitneho
#29.9.2026
#********************

print ("vitejte v kalkulacce spropitneho !")
celkova_castka = float(input("zadej celkovou castku ustu"))
spropitne = int(input("zadej spropitne v %"))
pocet_lidi = int(input("zadej pocet lidi u stolu: "))

spropitne_Kc = celkova_castka * spropitne / 100
print(spropitne_Kc)

celkova_castka += spropitne_Kc
print(celkova_castka)

zaplacena_castka = round (celkova_castka / pocet_lidi, 2)

print(f"zaplatitis 1/{pocet_lidi} z {celkova_castka} Kc ({zaplacena_castka} Kc)")