import random
import math
# Kérj be egy 2 jegyű (nehezebb: 3 jegyű) számot, és írd ki space-kkel elválasztva a számjegyeit!

def szokozok():
    i = 0
    szam: int = int(input("Adj meg egy háromjegyű számot!: "))
    while not szam>99 and szam<1000:
        szam: int = (input("Adj meg egy háromjegyű számot!: "))
    szam_str=str(szam)
    while i < len(szam_str):
        print(szam_str[i], end=" ")
        i += 1

# Egy tetszőleges Stringben meg kell számolni, hogy egy másik String hányszor fordul elő. 
# A feladat egyszerűsítése érdekében, most kis és nagybetűk között nem teszünk különbséget, bár azzal sem lenne túl bonyolult a feladat.       

def szovegkezeles(szoveg:str):
    karakter="e"
    karakterek_szama=szoveg.count(karakter)
    print(f"A szövegben: {karakterek_szama} db - {karakter} - betű van. ")

"""
# A következő feladat több programban is előfordulhat. Adott két időpont, melyeknél óra:perc:másodperc formában vannak megadva az időpontok.
#  A kérdés az, hogy mennyi idő telt el a két időpont között. 
# Az időpontok formátuma gyakorlatilag teljesen mindegy, csak feldolgozás kérdése, hogy előállítsuk belőle a megfelelő adatokat:

 ido1 = "7:35:40";  
 ido2 = "8:20:15";

# A feladat tehát: mennyi idő telt el a két időpont között? 
# Nem kell semmilyen komoly beépített vagy importált dátumkezelő osztályra gondolni, csak játék a számokkal 

def idokulonbseg():
"""

# Sorsolj ki egy pozitív egész számot, ami legfeljebb 1 milliárd lehet. Add össze a szám számjegyeit, majd a kapott szám számjegyeit ismét add össze. 
# Addig ismételd, amíg egyetlen számjegy nem marad, majd írd ki a végeredményt. 
# Az ellenőrzés megkönnyítése érdekében a köztes eredményeket is írd ki!

def szamjegyek_osszege():
    i:int = 0
    osszeg = 0
    szam:int = math.floor (random.random()*999999991 + 10)
    print(f"A kisorsolt szám: {szam}")
    while szam > 9:
        while szam > 0:
            utolso_szamjegy = szam % 10
            osszeg += utolso_szamjegy
            szam = szam // 10        
        print(f"A számjegyek összege: {osszeg}")
        szam = osszeg
        osszeg = 0

    print(f"A végeredmény: {szam}")




