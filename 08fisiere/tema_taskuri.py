# with open("categorii.txt", "a") as file:
#     while True:
#         categorie = input("Introduceti o categorie, pentru a termina apasa 0: ").lower()
#         with open("categorii.txt", "r+") as randuri:
#             if categorie in randuri.read():
#                 print("Valoare deja existenta")
#                 break
#
#         if categorie == "0":
#             break
#         else:
#             file.write(categorie + f"\n")

# import csv

# with open("lista_taskuri.txt", "a") as fisier:
#     while True:
#         task = input("Introduceti numele task-ului: ").lower()
#         data_limita = input("Introduceti data deadline-ului (dd.ll.aaaa hh:mm): ")
#         while True:
#             if len(data_limita) != 16:
#                 print("Formatul introdus nu este corect")
#                 data_limita = input("Introduceti data deadline-ului (dd.ll.aaaa hh:mm): ")
#             else:
#                 break
#         persoana = input("Introduceti numele persoanei responsabile de task: ").title()
#         categoria = input("Introduceti categoria din care face parte task-ul: ").lower()
#         while True:
#             with open("categorii.txt", "r+") as randuri:
#                 if categoria not in randuri.read():
#                     print("Categoria nu exista: ")
#                     categoria = input("Introduceti categoria din care face parte task-ul: ").lower()
#                 else:
#                     break
#         lista_task = [task, data_limita, persoana, categoria]
#         csv_writer = csv.writer(fisier, delimiter=",")
#         csv_writer.writerow(lista_task)
#
#         statut = input("Pentru a adauga un task apasa 1, pentru a continua apasa 0: ")
#         if statut == "0":
#             break

input("Alege o optiune din meniu: ")
