import random

numar_de_ghicit = random.randint(1, 10)


def joc():
    while True:
        numar_ghicit = int(input("Care este numarul?: "))
        if numar_ghicit < numar_de_ghicit:
            print("Numarul a fost prea mic.")
        elif numar_ghicit > numar_de_ghicit:
            print("Numarul a fost prea mare.")
        else:
            return f"Numarul este coret. Numarul ales de PC a fost:{numar_ghicit}"


print(joc())
