"""
Creează o aplicație care permite utilizatorului să adauge articole
 (cu preț și cantitate) la o factură și apoi să calculeze totalul.
"""


def adaugare_articole():
    factura = []
    while True:
        optiune_utilizator = input("Alege o optiune: ")
        if optiune_utilizator == "1":
            nume = input("Introdu numele atricolului: ")
            pret = float(input("Introdu pretul articolului: "))
            cantitate = int(input("Introdu cantitatea: "))
            factura.append({"nume": nume, "pret": pret, "cantitate": cantitate},)
        elif optiune_utilizator == "2":
            total = 0
            for articol in factura:
                total = total + articol["pret"] * articol["cantitate"]
            print(total)
        else:
            break
    return True


adaugare_articole()
