a = 15
b = 42
c = 7

# na zacatku prdpokladame, zeprvni cilo je jak minimum, tak maximum
min_val = a
max_val = a

# porovnavame s dryhym cislem 'b'
if b<min_val:
    min_val=b
elif b>max_val:
    max_val=b

# porovnavame s tretim cislem 'c'
if c<min_val:
    min_val=c
elif c>max_val:
    max_val=c

print("minimum je:", min_val)
print("maximum je:", max_val)  

