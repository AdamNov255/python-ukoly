# polarita promenne

cislo = float(input("zadej cislo"))

if cislo>0:
    print("kladna cisla")
else: 
    if cislo==0:
        print("nula")
    else:
        print("zaporne cislo")
cislo = -cislo

print(f"absolutni hofota je {cislo}")