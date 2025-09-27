#adattipusokl
'''tobsoros
komment'''


szoveg = "autorendszam"
szam = 15
logikai = True

print(szoveg)
print(szam)

szam *= 2
print(szam)
print(not logikai)
print(szam > 20)

print(szoveg[0])
print(szoveg[0:4])
print(szoveg[4:])
print(szoveg[4:8])
print(szoveg[-4:])

lista = ["hab", "kakao"]
print(lista[0] + lista[1])
lista += ["tejszin"]
print(lista)
print(lista[2], lista[0] + lista[1])

halmaz = {5 , 4 , 8 , 5, "korte"}
print(halmaz)

szotar = {"nev": "Feri", "kor": 43}
print(szotar)

eletkor = int(input("Adja meg eletkorat: "))
eletkor += 5
print(eletkor)
print(szotar["nev"], "kora:\n", eletkor, sep="-", end="\n")

print("valami".rjust(50,"_"))
print("valami".ljust(50,"_"))
print("valami".center(50,"_"))