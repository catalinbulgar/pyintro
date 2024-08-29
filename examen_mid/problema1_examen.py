"""
Scrie un program care sa afiseze un dictionar ce contine:
    1.Un numar dat de utilizator (nr. intreg pozitiv) care
    sa reprezinte numarul de chei cu prima cheie 1.
    2.Numarul maxim de chei admise este 15.
    3.Valorile pentru fiecare cheie reprezinta suma cumulativa
    a numerelor de la 1 pana la cheia respectiva
    (de exemplu, cheie 4 - valoare 10  deoarece 1+2+3+4 =10)
"""


def dict_constructor(x: int):
    dicti = {}
    if x < 0:
        print("Numarul trebuie sa fie pozitiv")
    elif x < 16:
        for i in range(1, x+1):
            suma = 0
            for j in range(0, i):
                suma += j
            dicti[i] = i + suma
        return dicti
    else:
        print("Numarul maxim de chei este 15")


nr_utilizator = int(input("Introdu un numar intreg pana la 15: "))
print(dict_constructor(nr_utilizator))
