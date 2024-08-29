"""
Scrie o functie care sa imparta o lista in doua liste in functie de un prag dat de la ytasattura:
Una cu elementele mai mici decat pragul dat si alta cu elementele mai mari sau egale cu acel prag
"""


def slice_list(prag: int, lista_mea):
    tuplu1 = list(x for x in lista_mea if x < prag)
    tuplu2 = list(y for y in lista_mea if y >= prag)
    return tuplu1, tuplu2


lista_ex = [5, 2, 9, 1, 5, 6]
pragul = int(input("Introduceti un numar intreg: "))
print(slice_list(pragul, lista_ex))
