"""
Implementati jocul X si 0.
Avem doi jucatori (X si 0) care isi vor scrie numele pe rand pe tabla de joc.
Tabla are de 3 X 3 casute, si este initial goala.
Jocul se incheie in momentul in care:

 - pe o linie avem doar X sau doar 0
 - pe o coloana avem doar X sau doar 0
 - pe o diagoanala avem doar X sau doar 0
- tabla s-a umplut si nu este indeplinita niciuna din conditiile de mai sus -> remiza
"""
import random

tabla = ["_" for _ in range(9)]

while True:

    print(f"{tabla[0]} {tabla[1]} {tabla[2]}")
    print(f"{tabla[3]} {tabla[4]} {tabla[5]}")
    print(f"{tabla[6]} {tabla[7]} {tabla[8]}")

    combinatii_castigatoare = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    while True:
        mutare = input("Alege un numar de la 1 la 9: ")
        if mutare.isdigit():
            mutare = int(mutare) - 1
            if mutare >= 0 <= 8:
                if tabla[mutare] == "_":
                    tabla[mutare] = "X"
                    break
                else:
                    print("Mutare invalida, incercati alt loc pe tabla")
            else:
                print("Numar invalid, introduceti un numar de la 1 la 9")
        else:
            print("Valoare invalida, introduceti un numar de la 1 la 9")

    print(f"\n")
    print(f"{tabla[0]} {tabla[1]} {tabla[2]}")
    print(f"{tabla[3]} {tabla[4]} {tabla[5]}")
    print(f"{tabla[6]} {tabla[7]} {tabla[8]}")
    print(f"\n")

    for conditie in combinatii_castigatoare:
        if tabla[conditie[0]] == tabla[conditie[1]] == tabla[conditie[2]] == "X":
            print("Jucatorul 1 a castigat!")
            exit()
        elif "_" not in tabla:
            print("Jocul incheiat in remiza")
            exit()

    mutari_posibile = [index for index, locuri_libere in enumerate(tabla) if locuri_libere == "_"]
    mutare = random.choice(mutari_posibile)
    tabla[mutare] = "0"

    for conditie in combinatii_castigatoare:
        if tabla[conditie[0]] == tabla[conditie[1]] == tabla[conditie[2]] == "0":
            print("Jucatorul 2 a castigat!")
            exit()
        elif "_" not in tabla:
            print("Jocul incheiat in remiza")
            exit()
