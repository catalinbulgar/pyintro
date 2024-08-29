"""
Scrie o functie care sa numere cate elemente pozitive sunt intr-un tuplu dat.
"""


def tuple_check(tuplu):
    return [i for i in tuplu if i > 0]


tuplul_meu = (-1, 3, -2, 4, 0, -6, 0)
rezultat = (len(tuple_check(tuplul_meu)))
print(f"Tuplul {tuplul_meu} are {rezultat} elemente pozitive")
