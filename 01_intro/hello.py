# print("Hello")
# print(1)
# print(type(1))
# print(1.4)
# print(type(1.4))
# print(1+2j)
# print(type(2j))
# print(1, type(1))
# print(1.3, type(1.3))
# print(1j,type(1j))
# print(float(1), type(1), type(float(1)))
# print(int(4.5), type(4.5), type(int(4.5)))
# print(5+2)
# print(5-6)
# print(3*4)
# print(5/3)
# print(7 % 4)
# print(7//4)
# print(4**3)
# print(1 == 5)
# print(5 == 5)
# print(1 != 5)
# print(4 > 3)
# print(6 < 3)
# print(5 <= 7)
# print(7 >= 7)
# print(3 <= 5)
# AND
# print(4 < 5 and 4 < 3)
# true and false => false
# false and true => false
# true and true => true
# false and false => false
# OR
# print(4 < 5 or 4 < 3 or 4 > 4)
# true or false => true
# false and true => true
# true and true => true
# false and false => false
# NOT
# print(not(4 < 5 and 4 > 2))
# print(not(5 > 4 > 2))
# print(not(4 > 5 and 3 > 2))
# print(7 is 7)
# print(7 is not 7)
# print(1 in [1, 2, 3])
# print("mere" in ["pere", "mere", "gutui"])
# print("mere" not in ["pere", "mere", "gutui"])
# print("p" in "paine")
# print("r" in "paine")
# print(str(0) in "paine0")
# variabila_noua = None
# variabila_Noua = "1.56"
# print(type(variabila_Noua))
# cuvant = "Ana are mere"
# cuvant = 'Ana are mere'
numar_mere = 3
numar_pere = 5
# cuvant = "Ana are " + str(numar_mere) + " mere si " + str(numar_pere)
# word = f'Ana are "{numar_mere}" mere si {numar_pere} pere'
# word = f'Ana are \'{numar_mere}\' mere si {numar_pere} pere'
word = "\tAna are {1} mere \nsi {0} pere".format(numar_mere, numar_pere)
# word = ("Ana are {0} mere si {0} pere").format(numar_mere)
print(word)
