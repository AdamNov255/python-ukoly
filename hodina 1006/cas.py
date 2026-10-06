cas = int(input("zadej cislo"))
if cas < 0 or cas > 24:
    print("zadny cas neni platny")
elif cas < 6:
    print("noc")
elif cas < 9:
    print("rano")
elif cas < 12:
    print("dopoledne")
elif cas < 13:
    print("poledne")
elif cas < 17:
    print("odloledne")
elif cas < 22:
    print("vecer")
else:
    print("noc")