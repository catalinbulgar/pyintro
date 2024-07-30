def is_valid(cnp_de_verificat: str) -> bool:
    if len(cnp_de_verificat) != 13 or not cnp.isdigit():
        return False

    cifra_sex = int(cnp_de_verificat[0])
    if cifra_sex not in range(1, 10):
        return False

    luna = int(cnp_de_verificat[3:5])
    if luna not in range(1, 13):
        return False

    ziua = int(cnp_de_verificat[5:7])
    if ziua not in range(1, 32):
        return False

    judet = int(cnp_de_verificat[7:9])
    if judet not in list(range(1, 47)) + list(range(51, 53)):
        return False

    cod_unic = int(cnp_de_verificat[9:12])
    if cod_unic not in range(1, 1000):
        return False

    numere_control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    suma_control = 0
    for numar in range(12):
        suma_control += int(cnp_de_verificat[numar]) * numere_control[numar]
    cifra_control = suma_control % 11
    if cifra_control == 10:
        cifra_control = 1
    if cifra_control != int(cnp_de_verificat[12]):
        return False
    else:
        return True


cnp = input("Introdu numarul CNP: ")
if is_valid(cnp):
    print(f"Numarul {cnp} este un CNP valid")
else:
    print(f"Numarul {cnp} nu este un CNP valid")
