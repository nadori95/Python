#  Kérjen be két (egész|valós) típusú számot és tárolja el, majd
#  írja ki, hogy melyik a nagyobb és melyik a kisebb szám!
#  Ha a két szám egyenlő, akkor azt is jelezze!

# Lehetséges megoldás:

print('Kisebb-nagyobb')
a: int = int(input('Kérem az elő számot = '))
b: int = int(input('Kérem a második számot = '))

if a > b:
    print(f'A nagyobb szám {a}, a kisebb {b}.')
elif b > a:
    print(f'A nagyobb szám {b}, a kisebb {a}.')
else:
    print('A két szám egyenlő.')

# Alternatív megoldás a max() és min() függvényekkel:

if a == b:
    print('A két szám egyenlő.')
else:
    print(f'A nagyobb szám {max(a,b)}, a kisebb {min(a,b)}.')
