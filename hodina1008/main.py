x_panacek = int(input("zadej souradnici x"))
y_panacek = int(input("zadej souradnici y"))

# nebezpecna plocha (kolizni oblast)
x1 = 2
x2 = 6
y1 = 2
y2 = 5

#test, zda doslo ke kolizi
if x_panacek>=x1 and x_panacek<=x2 and y_panacek>=y1 and y_panacek<=y2:
    print("doslo ke kolizi")
else:
    print("objekt mimo kolizni zonu...")