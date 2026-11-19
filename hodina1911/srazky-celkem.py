import urllib

url = "https://voskh.cz/envirotyden/index.php?lokalita=kutnahora"

# otevreni komunikace s webovym serverem, stazeni odpovedi ze serveru
odpoved = urllib.request.urlopen(url)

pocet_dnu = 0
srazky_celkem = 0

radek = odpoved.readline()              #ctu prvni radek (v Bytech)
while bool(radek):
    text_radku = radek.decode("utf-8")
    srazky = float(text_radku)
    if srazky >= 0:
        pocet_dnu += 1
        srazky_celkem += srazky
    radek = odpoved.readline()           #ctu dalsi radek
odpoved.close()

print(srazky_celkem/pocet_dnu)