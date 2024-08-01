"""
Creează un program care convertește o sumă dintr-o monedă
în alta folosind un curs de schimb fix.
"""


def schimb_valuar():
    suma = float(input("Introduceti suma de convertit: "))
    curs_schimb = float(input("Introduceti curs valutar: "))
    valoare = suma * curs_schimb
    return valoare


schimb = schimb_valuar()
print(schimb)
