a=float(input("vas vek: "))
b=input("jste student? :")
c=int(input("kolik vas bude ve skpunice? :"))
e=input("jaky bude den ? :")
d=500

if e=="sobota" or e=="nedele" or e=="neděle":
    d+=50
    typ_listku="vstupenka na vikend"

else:
    d
    typ_listku=""
if c>=4:
    typ="skupinova sleva"
    x=25
elif a>=65:
    typ="důchodcovská sleva"
    x=20
elif a<26 and b=="ano":
    typ="studentská sleva"
    x=30
else:
    typ="slevu"
    x=0

cena_jednoho= (d/100)*(100-x)
celokova_cena= cena_jednoho*c

if x>0:
    print(f"mate narok na {typ} v hodnote {x}%")
else:
    print("bohužel nemate narok na slevu")

print(f"cena jednoho vstupenky je {cena_jednoho}Kč")
print(f"celkova cena za vsechny vstupenky je {celokova_cena}Kč")
