cnp = input("Introduceti numarul CNP: ")
# verificam daca utilizatorul a introdus un numar de 13 cifre
if len(cnp) == 13 and cnp.isdigit():
    # verificam daca cifra sexului/secoluluio corespunde intervalului 1-9
    sex = int(cnp[0])
    if sex == 0:
        print("Cifra sexului/secolului nu corespunde, CNP invalid")
        exit()
    else:
        print("Cifra sexului/secolului valida")
# verificam daca cifrele lunii corespund intervalului 01-12
    luna = int(cnp[3:5])
    if luna not in range(1, 13):
        print("Cifrele luni nu corespund, CNP invalid")
        exit()
    else:
        print("Cifrele lunii sunt corecte")
# verificam daca cifrele zilei corespund intervalului 01-31
    ziua = int(cnp[5:7])
    if ziua not in range(1, 32):
        print("Cifrele zilei nu corespund, CNP invalid")
        exit()
    else:
        print("Cifrele zilei sunt valide")
# verficam daca cifrele judetului corespund listei cu coduri de judet
    judet = int(cnp[7:9])
    coduri_judet = list(range(1, 47))
    coduri_judet += [51, 52]
    if judet not in coduri_judet:
        print("Cifrele de judet nu sunt corecte, CNP invalid")
        exit()
    else:
        print("Cifrele de judet sunt corecte")
# calculam suma produselor dintre primele 12 pozitii ale CNP-ului cu omoloagele lor din lista numere_control
    numere_control = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    suma_control = 0
    for i in range(12):
        suma_control += int(cnp[i]) * numere_control[i]
# definim cifra de control ca fiind restul impartitii suma_control la 11
# exceptand situatia in care restul este 10, atunci cifra control devine 1
    cifra_control = suma_control % 11
    if cifra_control == 10:
        cifra_control = 1
# verificam daca cifra de control este egala cu ultima cifra a CNP-ului
    if cifra_control == int(cnp[12]):
        print("Cifra control corespunde, CNP-ul este valid")
    else:
        print("Cifra control incorecta, CNP-ul nu este valid")
        exit()
else:
    print("CNP-ul introdus nu este valid")
