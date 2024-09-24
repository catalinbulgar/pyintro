"""
1. Creati o clasa care sa calculeze si sa returneze operatia matematica de mai jos pentru
4 numere: [a(b+3)/c]*d.
Clasa trebuie sa aiba 2 metode: prima metoda este metoda speciala init.
Iar cea dea doua metoda este metoda speciala str.
Va rog sa aplicati cel putin doua exemple (doua obiecte).
Metoda init trebuie sa foloseasca parametrii default a=1,b=2,c=3,d=4 si trebuie sa suprime
orice eroare.
La aparitia unei erori trebuie sa afiseze textul: <>
Folositi clasa in trei exemple:
• cu patru parametrii numerici diferiti de cei default
• cu 3 parametrii non-numerici
• cu 2 parametrii numerici
"""


class CalculExpresieMatematica:

    def __init__(self, a=1, b=2, c=3, d=4):
        try:
            self.a = float(a)
            self.b = float(b)
            self.c = float(c)
            self.d = float(d)
            if self.c == 0:
                raise ZeroDivisionError("Diviziunea cu zero este interzisa.")
            self.rezultat = (self.a * (self.b + 3) / self.c) * self.d

        except (ValueError, ZeroDivisionError):
            self.rezultat = "<>"

    def __str__(self):
        return f"Rezultatul operatie este {self.rezultat}"


exemplu1 = CalculExpresieMatematica(10, 12, 14, 16)
print(exemplu1)
exemplu2 = CalculExpresieMatematica("a", "b", "c", 3)
print(exemplu2)
exemplu3 = CalculExpresieMatematica(5, 6)
print(exemplu3)
exemplu4 = CalculExpresieMatematica(1, 2, 0, 5)
print(exemplu4)
