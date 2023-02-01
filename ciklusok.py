
# addig ismétli a bekérést, amíg a felhasználó be nem ír egy 10nél nagyobb számot
x:int = 0
while x <= 10:
    x = int(input('írj be egy 10nél nagyobb számot: '))
print('köszi')

# 'végig megy' a lista minden egyes elemén
nevek = ['András', 'Béla', 'Cecil', 'Dénes']
for n in nevek:
    print(n)

# "számláló ciklus" while segítségével megvalósítva [0; 10)
i:int = 0
while i < 10:
    print(i)
    i += 1

# "számláló ciklus" for segítségével megvalósítva [0; 10)
for x in range(10):
    print(x)