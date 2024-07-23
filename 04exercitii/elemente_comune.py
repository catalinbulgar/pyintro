"""
Avand doua liste, afisati o lista a elementelor comune ambelor liste
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Rezultat
[1,2,3,5,8,13]
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# comun = []
# for element in a:
#     if element in b and element not in comun:
#         comun.append(element)
# print(comun)
print(list(set(a).intersection(set(b))))
