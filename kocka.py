import random
"""A feladat leadása github-on keresztül történik, github linket kérek!

Projekt neve: Sajat_nev_kockadobás

Készíts egy kockadobas listát, amiben 10 (teszteléshez, majd 1000) kockadobás eredményét tárolod. Töltsd fel adatokkal!
"""
dobasok = []
def dobaslista():
    print(dobasok)


def dobas(dobas_szama):

    i = 0
    while i < dobas_szama:
        szam = int(random.random()*6)+1
        dobasok.append(szam)
        i += 1


def hanyszor_szerepel(keresett_szam):
    i = 0
    db = 0
    while i < len(dobasok):
        if dobasok[i] == keresett_szam:
            db += 1
        i += 1
    # print(f"A keresett szám: {keresett_szam} -    {db}x szerepel a listában")
    return db

def csillag(keresett_szam):
    db = hanyszor_szerepel(keresett_szam)
    jel = "* "
    print(jel * db)


def stat_szamol():
    i = 0
    db1, db2, db3, db4, db5, db6 = 0, 0, 0, 0, 0, 0
    while i < len(dobasok):
        match dobasok[i]:
            case 1:
                db1 += 1
            case 2:
                db2 += 1
            case 3:
                db3 += 1
            case 4:
                db4 += 1
            case 5:
                db5 += 1
            case 6:
                db6 +=1
        i += 1
    statisztika_db = db1, db2, db3, db4, db5, db6

    return statisztika_db


def savdiagram():
    lista = stat_szamol()
    jel = "* "
    i = 0
    while i < len(lista):
        print(f"{i+1}: {lista[i]*jel}")
        i += 1
"""
Készíts függvényt, ami visszaadja, hogy hányszor dobtuk a paraméterében megadott számot!
Készíts egy metódust, amely kiír a képernyőre annyi csillagot, ahányszor dobták a paraméterében kapott számot. 
Készíts metódust, ami megjeleníti a képernyőn egy sávdiagram formájában a kockadobások eredményét: 
1: **********
2:********
3:*****************
4:********************
5:************
6:********************
"""



"""
Volt-e olyan eset, hogy kétszer egymás után ugyanazt a számot dobtuk? 
Mekkora volt a leghosszabb ilyen sorozat? Melyik számot dobtuk ekkor?  - nehéz
Készíts "cinkelt" kockát! 6- kétszer akkora nagyobb valószínűséggel dobjon, mint bármelyik más számot! Jelentítsd
 meg ehhez a dobókockéhoz tartozó statisztikát is! Alakítsd át úgy az eddig megírt függvényeket, hoyg most is 
 használhatsd őket!
 """