print("== SIMULACE PRO CISARE FRIDNICHA II. ==")
meisce=int(input("Na kolik mesicu ma byt simulace? :"))
a = 1
b = 1
pocet_mesicu=0
dokonceno = False
 
while dokonceno == False:
    pocet_mesicu+=1
 
    if pocet_mesicu==meisce:
        dokonceno = True
 
    if pocet_mesicu > 2:
     temp = a + b
     a = b
     b = temp
 
    print(" ")
    print(f"mesic {pocet_mesicu}:  {b} par(u) | " + "🐇"*b)
 
print(" ")
print(f"Na cisarkem ostrove bude celkem {b} paru")
 