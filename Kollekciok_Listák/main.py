def main():
    #  Lista létrehozása:
    lista1 = ['barack', 'körte', 'szilva', 'alma', 'szőlő']  # Elemekkel inicializált lista
    lista2 = []   # Üres lista
    lista3 = list()  # list() konstruktorral létrehozott üres lista
    lista4 = list({'a', 'e', 'i', 'o', 'u'})  # list() konstruktorral halmazból létrehozott lista

    # Teljes lista kiírása
    print(lista1)  # ['barack', 'körte', 'szilva', 'alma', 'szőlő']

    # Hivatkozás lista elemeire (indexelés)
    # Listák elemit 0-tól indulva egész számokkal indexeljük:
    print(lista1[0])  # barack
    # indexelés index tartománnyal
    print(lista1[1:3])  # ['körte', 'szilva']
    print(lista1[1:])  # ['körte', 'szilva', 'alma', 'szőlő']
    print(lista1[:2])  # ['barack', 'körte']
    # negatív indexet is használhatunk:
    print(lista1[-1])  # szőlő
    print(lista1[-3:-1])  # ['szilva', 'alma']

    # Értékadás
    lista1[0] = 'alma'
    print(lista1)
    lista1[0] = True  # A lista elemi bármikor válthatják típusukat
    lista1[1] = 123
    print(lista1)

    # Lista bejárása index nélkül
    for i in lista1:
        print(f'{i} ', end='')  # True 123 szilva alma szőlő
    print()  # Soremelés
    # Lista bejárása indexekkel
    for index, item in enumerate(lista1):
        print(f'lista1[{index}]={item} ', end='')  # True 123 szilva alma szőlő
    print()  # Soremelés

    # Tartalmazás vizsgálat az IN oprátorral
    if 'alma' in lista1:
        print('Az alma érték megtalálható a listában!')

    # Lista eleminek száma, lista "hossza": len() függvény
    print(F'A lista1 lista elemeinek száma: {len(lista1)}')  # 5

    # Elem hozzáadása a lista végéhez: append()
    lista2.append(23)
    lista2.append(34)
    lista2.append(45)
    print(lista2)  # [23, 34, 45]

    # Elem beszúrása a listába: insert()
    lista2.insert(2, 99)  # A megadott indexű (2) elem elé szúr be
    print(lista2)  # [23, 34, 99, 45]
    # Beszúrás a lista elejére
    lista2.insert(0, 99)
    print(lista2)  # [99, 23, 34, 99, 45]

    # Megadott értékű elem első előfordulálsnak törlése: remove()
    lista2.remove(99)
    print(lista2)  # [23, 34, 99, 45]

    # Utolsó elem vagy a megadott indexű elem törlése
    lista2.pop()  # Utolsó elem törlése
    print(lista2)  # [23, 34, 99]
    lista2.pop(1)  # Megadott indexű (1) elem törlése
    print(lista2)  # [23, 99]

    # Lista ürítése (minden elem törlése)
    lista2.clear()
    print(lista2)  # []

    # Teljes lista törlése
    del lista2
    #  print(lista2)  # Hiba: UnboundLocalError: local variable 'lista2' referenced before assignment

    # Másolat készítése listából
    lista2 = lista1  # Így nem készül másolat, hanem a lista2 ugyanazon referencára (memóriacímre) mutat
    lista2.pop()
    print(lista1)  # [True, 123, 'szilva', 'alma']
    print(lista2)  # [True, 123, 'szilva', 'alma']

    # Másolat 1. módszer: copy()
    lista2 = lista1.copy()
    lista2.pop()
    print(lista1)  # [True, 123, 'szilva', 'alma']
    print(lista2)  # [True, 123, 'szilva']

    # Másolat 2. módszer: list() konstruktorral
    lista5 = list(lista1)
    print(lista5)  # [True, 123, 'szilva', 'alma']

    # Megadott értékű elem darabdszáma: count()
    lista6 = [4, 5, 6, 5, 5, 3, 4, 5, 6]
    print(lista6.count(5))  # 4

    # Megadott elem első előfordulásának az indexe: index()
    print(lista6.index(6))  # 6

    # Lista bővítése másik listával: extend()
    lista_A = ["a", "b", "c"]
    lista_B = [1, 2, 3]
    lista_A.extend(lista_B)
    print(lista_A)  # ['a', 'b', 'c', 1, 2, 3]

    # Lista "megfordítása": reverse()
    print(lista6)  # [4, 5, 6, 5, 5, 3, 4, 5, 6]
    lista6.reverse()
    print(lista6)  # [6, 5, 4, 3, 5, 5, 6, 5, 4]

    # Lista rendezése: sort()
    lista6.sort()  # Növekvő sorrend
    print(lista6)  # [3, 4, 4, 5, 5, 5, 5, 6, 6]

    lista6.sort(reverse=True)  # Csökkenő sorrend
    print(lista6)  # [6, 6, 5, 5, 5, 5, 4, 4, 3]


if __name__ == '__main__':
    main()
