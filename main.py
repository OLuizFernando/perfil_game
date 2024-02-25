import csv

with open('cartas.csv', 'r', encoding='UTF-8') as cartas:
    cartas_csv = csv.reader(cartas, delimiter=';')
    for row in cartas_csv:
        print(row[11])