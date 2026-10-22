# vek = int(input("Zadej svůj věk: "))
# if vek < 18:
#    print("jsi nezletily.")

vek = int(input("Zadej svůj věk: "))
while vek < 18 and vek >= 0:
    print("jsi nezletily.")
    vek = int(input("Zadej svůj věk znovu(ukocim zapornou hodnotou): "))
if vek > 0:
    print("pristup povolen")
else:
     print("pristup zamitnut")


