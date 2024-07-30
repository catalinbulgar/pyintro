my_var = input("Adauga un numar: ")
try:
    conversie_int = int(my_var)
    a = int(input("A doua valoare: "))
    impartire = conversie_int / a
    print(variabila)
except ValueError:
    print("Eroare de valoare")
except NameError:
    print("Variabila nu este declarata")
    variabila = None
except ZeroDivisionError:
    print("Impartirea la zero nu este permisa")
    while a == 0:
        a = int(input("A doua valoare: "))
    impartire = conversie_int / a
    print(impartire)
except Exception as e:
    print(e)
else:
    print("Codul nu are exceptii")
finally:
    print("Se executa indiferent")
print(variabila)
