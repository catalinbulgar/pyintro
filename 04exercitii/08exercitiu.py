"""
5. Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea
de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare
acest sir de caractere:
“”” 1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi “””
Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
- daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”
"""
mesaj = "1 – Afisare lista de cumparaturi\n" "2 – Adaugare element\n" "3 – Stergere element\n"\
        "4 – Sterere lista de cumparaturi\n" "5 - Cautare in lista de cumparaturi\n"
lista_de_cumparaturi = ["suc", "apa", "carne", "lapte"]
print(mesaj)

selectie = input("Introduceti un numar de la 1 la 5: ")
if selectie == "1":
    print(lista_de_cumparaturi)
elif selectie == "2":
    adaugare_element = input("Adaugare element: ")
    lista_de_cumparaturi.append(adaugare_element)
    print(lista_de_cumparaturi)
elif selectie == "3":
    print(lista_de_cumparaturi)
    stergere_element = input("Stergere element: ")
    if stergere_element in lista_de_cumparaturi:
        lista_de_cumparaturi.remove(stergere_element)
        print(lista_de_cumparaturi)
elif selectie == "4":
    print(lista_de_cumparaturi)
    lista_de_cumparaturi.clear()
    print(lista_de_cumparaturi)
elif selectie == "5":
    element_cautat = input("Introdu elementul de cautat: ")
    if element_cautat in lista_de_cumparaturi:
        print("Elementul se afla in lista de cumparaturi")
    else:
        print("Elementul nu se afla in lista cumparaturi")
else:
    print("Alegerea nu exista. Reincercati")
