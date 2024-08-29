"""
1.Scrieti un program care sa afiseze un dictionar ce contine:
- un numar dat de utilizator (numar intreg poztitiv), de chei, cu prima cheie 1
- numarul maxim de chei admise: 20
- valorile pentru fiecare cheie in parte reprezinta patratul cheii (ex. cheie 3 - valoare 9)
(2 puncte)
"""


# def nr_chei(x: int) -> dict:
#     dictionar = {}
#     if x < 0:
#         print("Numarul trebuie sa fie pozitiv ")
#
#     elif x < 21:
#         for i in range(1, x+1):
#             dictionar[i] = i * i
#
#         return dictionar
#     else:
#         print("Numarul maxim este 20")
#
#
# numar_utilizator = int(input("Introduceti u n numar intreg pozitiv intre 1-20: \n"))
# print(nr_chei(numar_utilizator))

"""
2.Scrieti o functie care sa calculeze suma tuturor numerelor dintr-un tuplu dat.
model:
tuple_example = (8, 2, 3, 0, 7)
result = 20
"""


# def sum_tuple(my_tuple):
#     return sum(my_tuple)
#
#
# my_tuple1 = (8, 2, 3, 0, 7)
# print(sum_tuple(my_tuple1))


"""
3.Scrieti o functie, care sa separe o lista data de utilizator, in doua parti, 
astfel incat lungimea primei liste sa fie egala cu un numar dat. 
model:
list_example = [1, 1, 2, 3, 4, 4, 5, 1]
first_list_length = 3
result = ([1, 1, 2], [3, 4, 4, 5, 1])
"""


# def slice_list(slice_point: int, lista_mea: list) -> tuple:
#     lista1 = lista_mea[:slice_point]
#     lista2 = lista_mea[slice_point:]
#     return lista1, lista2
#
#
# lista = [str(caracter) for caracter in input("Introduceti lista dorita:\n").split(",")]
# print(lista)
# numar_separare = int(input("Introduceti punctul de separare:\n"))
# print(slice_list(numar_separare, lista))


"""
Se dă un şir cu cel mult 10 caractere. Să se determine câte vocale conţine. (1 punct)
"""


# def count_vowel() -> str:
#     sir = input("Introduceti un sir de maxim 10 carctere: ").lower()
#     vowels = "aeiou"
#     count = 0
#     if len(sir) <= 10:
#         for i in sir:
#             if i in vowels:
#                 count = count + 1
#     else:
#         return "Sirul depaseste 10 caractere"
#     return str(count)
#
#
# print(count_vowel())


"""
Sa se scrie un program care sa calculeze impartirea dintre trei numere.
Daca valorile sunt egale, returnati de trei ori rezultatul. Impartirea la 0 va duce la rezultatul 0. (1 punct)
"""


# def impartire_numere(a, b, c) -> float:
#     if a == b == c:
#         cat = a / b / c
#         return cat * 3
#     elif a == 0 or b == 0 or c == 0:
#         return 0
#     else:
#         cat = a / b / c
#         return cat
#
#
# print(impartire_numere(0, 2, 3,))


"""
Se da sirul de numere n care contine [1, 2, 3, 4, 5, 6, 7].
Sa se insereze in acest sir dupa fiecare element par, dublul acestuia (2 puncte)
"""


def double_even(lista: list) -> list:
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            lista.insert(i+1, lista[i] * 2)
            i += 1
        i += 1
    return lista


lista_mea = [1, 2, 3, 4, 5, 6, 7]
print(double_even(lista_mea))
