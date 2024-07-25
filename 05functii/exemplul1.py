# print("Mesaj")
# input("Adauga un numar: ")

def my_function(nr_mere: str = "2", nume: str = "Ioana") -> (str, str):
    """
    :param nr_mere: numarul de mere
    :param nume: numelele celui care detine merele
    :return: propozitii
    """
    return (f"{nume} are {nr_mere} mere",
            f"{nume} are {nr_mere} pere")


a, c = my_function("3")
b, d = my_function("7", "Maria")
e, f = my_function(nume="Gelu")
# print(a)
# print(b)
# print(c)
# print(d)
print(f, e)
