try:
    eredmeny = 10 / 0 #ertek akkor nevhiba
except ZeroDivisionError:
    print("HIBA: Nullaval valo osztas")
except NameError:
    print("HIBA: nevhiba")
else:
    print(eredmeny)