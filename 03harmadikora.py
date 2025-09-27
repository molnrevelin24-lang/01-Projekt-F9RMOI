
'''import p03

szam = 10
while szam > 2:
    szam -= 1
    if szam == 4:
        continue
    if szam == 3:
        break
    print(szam)
else:
    print("Ciklus vege")

while True:
    szam += 1
    print(szam)
    if szam == 30:
        break
'''

def szam_bekerese(legnagyobb_szam):
    szam = input("Adj meg egy szamot:")
    if szam.isdigit():
        szam = int(szam)
        if szam == 0:
            print("Hiba")
        elif szam > legnagyobb_szam:
            print("A szam tul nagy")
        else:
            print("Jo szamot adtal meg")
    else:
        print("Nem szam!")
    return szam

def szamologep():
    muvelet = input("Milyen muveletet akar vegrehajtani (+,-,*,/):")
    egyik_szam = szam_bekerese(10)
    masik_szam = szam_bekerese(100)
    if muvelet == "+":
        eredmeny = egyik_szam + masik_szam
    elif muvelet == "-":
        eredmeny = egyik_szam - masik_szam
    elif muvelet == "*":
        eredmeny = egyik_szam * masik_szam
    else:
       eredmeny = egyik_szam / masik_szam
    print(f"Eredmeny: {egyik_szam} {muvelet} {masik_szam} = {eredmeny}")

def veletlenszam(max):
    import random
    szam = random.randint(0, max)
    return szam

def egesz_szam_bekerese():
    while True:
        szam = input("Adjon meg egy egesz szamot")
        try:
            szam = int(szam)
            break
        except ValueError:
            print("Nem egesz szam!")
    return szam


# A proram indítása
if __name__ == "__main__":
    print(egesz_szam_bekerese())