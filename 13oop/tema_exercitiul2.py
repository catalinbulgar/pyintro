"""
Problema 2.
• Creati o clasa ce va reprezenta un catalog de prajituri.
La crearea unui obiect al acestei clase, se vor solicita trei argumente, reprezentand nume (sir
de caractere), preț (integer) si gramaj (integer). Fiecare obiect creat va fi adaugat intr-o lista
mentinuta de o variabila a clasei.
Clasa trebuie sa detina o metoda care sa poate afisa toate prăjiturile sortand în funcție de
nume, gramaj sau pret.
• Creati a doua clasa care mosteneste prima clasa si care se va numi Tort.
Aceasta clasa va avea un atribut denumit etajat, care default va fi False și un alt atribut care
se numește glazura (sir de caractere) si care are default, valoarea „ciocolata”. Aceste atribute
trebuiesc implementate printr-o metoda de setare cu parametrii de intrare. O alta metoda
permite
citirea acestora.
• Creati a treia clasa care mosteneste prima clasa care se va numi Fursec. Aceasta va
mosteni intocmai prima clasa fara a modifica/ adauga nimic.
Verificari:
Creati 3 obiecte ale clasei Tort si trei obiecte ale clasei Fursec.
Afisati prajiturie dupa gramaj.
Afisati prajiturie dupa pret.
Folositi pentru un obiect de tip tort modificarea atributelor etajat in True si glazura in “cacao”,
apoi pentru acest obiect folositi metoda de afisare a atributelor glazura si etajat.
De asemenea, folositi metoda de setare/afisare si pentru un alt obiect de tip tort
"""


class CatalogPrajituri:
    lista_prajituri = []

    def __init__(self, nume, pret, gramaj):
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj
        self.adauga_in_lista()

    def adauga_in_lista(self):
        CatalogPrajituri.lista_prajituri.append(self)

    def afisare_prajituri(self, criteriu_sortare):
        if criteriu_sortare == "nume":
            prajituri_sortate = sorted(self.lista_prajituri, key=lambda praji: praji.nume)
        elif criteriu_sortare == "pret":
            prajituri_sortate = sorted(self.lista_prajituri, key=lambda praji: praji.pret)
        elif criteriu_sortare == "gramaj":
            prajituri_sortate = sorted(self.lista_prajituri, key=lambda praji: praji.gramaj)
        else:
            print("Criteriu Invalid")
            return

        for prajitura in prajituri_sortate:
            print(f"Nume {prajitura.nume} - {prajitura.pret} lei - {prajitura.gramaj} gr\n")


class Tort(CatalogPrajituri):

    def __init__(self, nume, pret, gramaj):
        super().__init__(nume, pret, gramaj)
        self.etajat = False
        self.glazura = "ciocolata"

    def setare_parametrii(self, etajat=False, glazura="ciocolata"):
        self.etajat = etajat
        self.glazura = glazura

    def citire_parametrii(self):
        return f"Glazura: {self.glazura}\n Etajat: {self.etajat}"


class Fursecuri(CatalogPrajituri):
    pass


tort1 = Tort("Tort rawvegan", 120, 600)
tort2 = Tort("Tort ciocolata", 100, 900)
tort3 = Tort("Tort fructe padure", 120, 1000)

fursec1 = Fursecuri("Fursec cu coacaze", 15, 75)
fursec2 = Fursecuri("Fursec fulgi ciocolata", 10, 60)
fursec3 = Fursecuri("Fursec vanilie", 12, 75)

print(tort1.afisare_prajituri("nume"))
print(tort1.afisare_prajituri("gramaj"))
print(tort1.afisare_prajituri("pret"))

print(tort1.setare_parametrii(True, "cacao"))
print(tort1.citire_parametrii())
