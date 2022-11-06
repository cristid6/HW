"""Sa se afiseze adresele care gazduiesc mai mult de 3 institutii si numele institutiilor gazduite."""

import csv
import collections

entity = []
address = []

with open("lista_ep_portal_01102022.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=";")
    for line in reader:
        entity.append(line[2])
        address.append(str(line[4].split(",")[0:4]))

repeated_address =  [item for item, count in collections.Counter(address).items() if count > 2]

for item in repeated_address:
    print(item)
    for element in address:
        if element == item:
            print(entity[address.index(element)])
            address[address.index(element)] = "checked"

