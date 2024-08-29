"""
1.
Creati un program in care utilizatorul sa introduca o adresa de email de formatul
litere_sau_cifre@litere_sau_cifre.litere.
Validati acest sir de caractere si informati utilizatorul de raspuns. @ sau .(punct) trebuie sa
exista o singura data in sirul de caractere
> trebuie sa contina @ si . o singura data
> tot ce este inainte de . contine litere_sau_cifre, cu exceptia @
> tot ce urmeaza dupa . contine doar litere
> trebuie sa avem caracter scris inainte de @
> trebuie sa avem caracter(e) scris(e) intre @ si .
> trebuie sa avem minim 2 litere dupa .
"""
# import random

# import re
# email = input("Introduceti adresa de email: ")
# pattern =r' ^[a-zA-Z0-9_]+@[a-zA-Z0-9_]{2,}(?:\.[\a-zA-Z0-9_]){1}[a-zA-Z_]{1,}$'

# if re.search(pattern, email):
#     print("Adresa de email valida")
# else:
#     print("adresa de email invalida")

"""
2.
Scrieti un program care sa valideze nr de telefon al unui utilizator scris de la tastatura.
+40123456789
> incepe cu +40 (primele 3 caractere sunt +40)
> are 12 caractere
> sa aiba caracterele de la 3 la 12 sa fie doar cifre
"""

# import re

# pattern = r"^(\+40){1}[0-9]{9}$"
# numar = input("Introduceti numarul de telefon: ")

# if re.search(pattern, numar):
#     print("Numarul de telefon este valid")
# else:
#     print("Numarul de telefon nu este valid")

"""
3.
Se cer 2 nr intregi de la tastatura. Sa se calculeze produsul daca produsul dintre cele 2
numere este mai mic sau egal cu 1000, altfel, sa se returneze suma acestora.
"""

# numar1 = int(input("Introduceti primul numar: "))
# numar2 = int(input("Introduceti al doilea numar: "))

# print(numar1 * numar2) if numar1 * numar2 <= 1000 else print(numar1 + numar2)

"""
4.
scrieti un program care itereaza prin primele
10 numere. La fiecare iteratie afiseaza
suma dintre iteratorul curent si urmatorul iterator din sir.
"""
# suma = 0
# for i in range(10):
#     suma += i
#     print(suma)

"""
5.
Sa da de la tastatura un string. Sa se elimine caracterele din string pornind de la 0 pana
la n, unde n e dat si el de la tastatura
"""

# string = input("Introduceti un string: ")
# n = int(input("Introduceti indexul pana la care sa se elimine caractere: "))

# string_nou = string[n:]
# print(string_nou)

"""
6.
sa se scrie o functie care sa returneze True in cazul in care primul si ultimul element
dintr-o lista sunt la fel. Altfel, returnati False.
"""


# def first_last(lista) -> bool:
#     if lista[0] == lista[-1]:
#         return True
#     else:
#         return False


# lista = ["lapte", "branza", "oua", "banane", "avocado", "mere", "pere", "lapte"]
# random.shuffle(lista)
# print(first_last(lista))

"""
7.
scrieti un program care sa extraga inversul dintr
un nr.
Exemplu: 7536 trebuie afisati 6 3 5 7
"""

# numar = input("Introduceti un numar: ")
# for i in reversed(numar):
#     print(i, end=" ")

"""
8.
Realizati un program care sa gaseasca al doilea cel mai mic numar din lista.
list_1 = [-8, 1, 2, -2, 0] -> ex.: -2
ist_2 = [1, 1, 0, 0, 2, 2, 2]-> ex.: 0
list_3 = [1, 1, 0, 9, 4, 5]
list_4 = [1, 4, 0, 23, 6, 34]
"""
# list_1 = [-8, 1, 2, -2, 0]
# list_2 = [1, 1, 0, 0, 2, 2, 2]
# list_3 = [1, 1, 0, 9, 4, 5]
# list_4 = [1, 4, 0, 23, 6, 34]


# def second_min(list) -> str:
#     list.sort()
#     return list[1]


# print(second_min(list_2))

"""
9.
Realizati un program care sa creeze o lista, con
catenand o lista data, cu nr. de la 1 la n
exemplu:
list_var = ['p', 's']
n = 5
result = ['p1', 's1', 'p2', 's2', 'p3', 's3', 'p4', 's4', 'p5', 's5']
"""

# lista_var = ["p", "s"]
# lista_concatenare = []
# n = int(input("Alegeti un numar: "))
# for i in range(1, n+1):
#     for item in lista_var:
#         lista_concatenare.append(f"{item}{i}")

# print(lista_concatenare)

"""
10.
Scrieti un program care sa faca split dupa al n-lea element intr-o lista:
lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
result = [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""

# lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# n = int(input("Indroduceti numarul index-ului unde sa se faca slice-ul: "))
# rezultat = [[] for i in range(n)]
# for j in range(len(lista_start)):
#     rezultat[j % n].append(lista_start[j])
# print(rezultat)

"""
11.
Realizati un program care sa sorteze o lista de dictionare folosind functia Lambda.
models = [{'make':'Huawei', 'model':2, 'color':'Black'}, {'make':'Apple', 'model':'14', 'color':'Gold'},
{'make':'Samsung', 'model': 7, 'color':'Blue'}]
"""
# models = [{'make': 'Huawei', 'model': 2, 'color': 'Black'},
#           {'make': 'Apple', 'model': '14', 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# print(sorted(models, key=lambda x: x['make']))

"""
12.
se da un cuvant de la tastatura. sa se indice cate vocale si cate consoane contine.
"""


# def count_vocale_consoane():
#     cuvant = input("Introduceti un cuvant: ").lower()
#     vocale = "aeiou"
#     count_vocale = 0
#     count_cons = 0
#     if cuvant.isalpha():
#         for i in cuvant:
#             if i in vocale:
#                 count_vocale = count_vocale + 1
#             else:
#                 count_cons = count_cons + 1
#         return f'Cuvantul are {count_vocale} vocale si {count_cons} consoane'
#     else:
#         return f'Cuvantul contine si alte caractere'


# print(count_vocale_consoane())

"""
13.
se da un string de la tastatura. sa se calculeze suma digitilor din acel string
"""

# string = input("Introduceti un sir de numere: ")
# suma = 0
# if string.isdigit():
#     for i in string:
#         suma += int(i)
# else:
#     print("Stringul contine si alte caractere non numerice")
#
# print(f'sirul de numere introdus este: {string}')
# print(f'suma digitilor din string este: {suma}')
