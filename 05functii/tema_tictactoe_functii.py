import random


def initializare_tabla():
    return ["_" for _ in range(9)]


def tabla_joc(tabla):
    print(f"\n")
    print(f"{tabla[0]} {tabla[1]} {tabla[2]}")
    print(f"{tabla[3]} {tabla[4]} {tabla[5]}")
    print(f"{tabla[6]} {tabla[7]} {tabla[8]}")
    print(f"\n")


def verificare_castigator(tabla, jucator):
    combinatii_castigatoare = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for conditie in combinatii_castigatoare:
        if tabla[conditie[0]] == tabla[conditie[1]] == tabla[conditie[2]] == jucator:
            return True
        else:
            return False


def verificare_remiza(tabla):
    return "_" not in tabla


def mutare_jucator(tabla):
    while True:
        mutare = input("Alege un numar de la 1 la 9: ")
        if mutare.isdigit():
            mutare = int(mutare) - 1
            if 0 <= mutare < 9:
                if tabla[mutare] == "_":
                    return mutare
                else:
                    print("Mutare invalida, incercati alt loc pe tabla")
            else:
                print("Numar invalid, introduceti un numar de la 1 la 9")
        else:
            print("Valoare invalida, introduceti un numar de la 1 la 9")


def mutare_computer(tabla):
    mutari_posibile = [index for index, locuri_libere in enumerate(tabla) if locuri_libere == "_"]
    return random.choice(mutari_posibile)


def main():
    tabla = initializare_tabla()
    tabla_joc(tabla)
    while True:
        mutarejucator = mutare_jucator(tabla)
        tabla[mutarejucator] = "X"
        tabla_joc(tabla)
        if verificare_castigator(tabla, "X"):
            print("Jucatorul 1 a castigat!")
            break
        if verificare_remiza(tabla):
            print("Jocul s-a incheiat in remiza")
            break

        mutarecomputer = mutare_computer(tabla)
        tabla[mutarecomputer] = "0"
        tabla_joc(tabla)
        if verificare_castigator(tabla, "0"):
            print("Jucatorul 2 a castigat!")
            break
        if verificare_remiza(tabla):
            print("Jocul s-a incheiat in remiza")
            break


main()
