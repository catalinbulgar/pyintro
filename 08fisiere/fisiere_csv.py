import csv

new_cars = [
    ["Dacia", "Logan", 2005, 75],
    ["Renault", "Clio", 2005, 75]
]
with open("data_csv", "a", newline="") as csv_file1:
    csv_writer = csv.writer(csv_file1, delimiter=",")
    for new_car in new_cars:
        csv_writer.writerow(new_car)


def csv_reader():
    with open("data_csv", "r", newline="") as csv_file:
        rows = csv.reader(csv_file, delimiter=",")
        for row in rows:
            print(row)


csv_reader()
