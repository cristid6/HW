# Cool
# Se consideră un șir A format din N elemente naturale nenule.
# Numim secvență de lungime K a șirului A orice succesiune de elemente consecutive
# din șir de forma Ai, Ai+1, ..., Ai+K-1.
# O secvență o numim secvență cool dacă elementele
# care o compun sunt distincte și pot fi rearanjate astfel
# încât să alcătuiască o secvență continuă de numere consecutive.
# De exemplu, considerând șirul
# A = (3, 1, 6, 8, 4, 5, 6, 7, 4, 3, 4), atunci secvența
# (8, 4, 5, 6, 7) este o secvență cool deoarece conține
# elemente distincte ce pot fi rearanjate astfel încât să alcătuiască
# șirul de numere consecutive 4, 5, 6, 7, 8,
# pe când secvențele (4, 3, 4), (6, 7, 4, 3) nu sunt considerate secvențe cool.
# Cerință:
#     Pentru o valoare dată K să se verifice dacă secvența
#     A1, A2 ... AK este secvență cool.
#     Dacă secvența este cool, atunci se va afișa
#     cea mai mare valoare ce aparține secvenței.
#     Dacă secvența nu este cool, atunci se va afișa numărul
#     elementelor distincte din secvența
# A1, A2, ..., AK, adică numărul elementelor care apar o singură dată.
# Date de intrare:
#     Se citesc N și K de la tastatură
#     care vor determina numărul de elemente din sir
#     respectiv lungimea secvenței cool de verificat.
# Exemple:
# INPUT:
# 7 4
# 6 4 5 7 8 3 5
# OUTPUT:
# 7
# Secvența 6 4 5 7 este cool.
# Valoarea maximă din secvență este 7
# INPUT:
# 7 6
# 6 4 5 7 5 4 3
# OUTPUT:
# 2
# Secvența 6 4 5 7 5 4 nu este secvență cool.
# Numărul valorilor distincte din secvență este 2.
# Valorile distincte sunt: 6, 7


import random

while True:
    try:
        n = int(input('Enter the length of the list:'))
        k = int(input('Enter the length of the sequence:'))
        if k <= n:
            break
        else:
            print(f'The length of the list must be at least equal with the length of the sequence! Try again!')
            continue
    except Exception:
        print('Please enter only integer numbers!')


random_list = []
for i in range(1, n+1):
    random_list.append(random.randint(1, n))

print(f'The random generated list is: {random_list}.')

sequence_list = []
all_sequences = []
i = 0

print('The sequences are:')

while True:
    for element in range(i, k):
        sequence_list.append(random_list[element])
    print(sequence_list)
    all_sequences.append(sequence_list)
    sequence_list = []
    i += 1
    k += 1
    if k > len(random_list):
        break

all_sequences_repeating_values = []
all_sequences_distinct_values = []
all_sequences_sorted_values = []
all_sequences_consecutive_values = []

for sequence_list in all_sequences:
    repeating_values = set()
    distinct_values = []
    sorted_values = []
    i_index = 0
    for i in range(i_index, len(sequence_list)):
        for j in range(i_index+1, len(sequence_list)):
            if sequence_list[i] == sequence_list[j]:
                repeating_values.add(sequence_list[i])
        i_index += 1

    if len(repeating_values) > 0:
        all_sequences_repeating_values.append(repeating_values)
        for element in sequence_list:
            sorted_values.append(element)
            if element not in repeating_values:
                distinct_values.append(element)
        sorted_values.sort()
        all_sequences_sorted_values.append(sorted_values)
        all_sequences_distinct_values.append(distinct_values)
    else:
        for element in sequence_list:
            sorted_values.append(element)
        sorted_values.sort()
        all_sequences_sorted_values.append(sorted_values)
        all_sequences_repeating_values.append(None)
        all_sequences_distinct_values.append(sequence_list)

for sorted_values in all_sequences_sorted_values:
    consecutive_values = 0
    for i in range(0, len(sorted_values)-1):
        if sorted_values[i+1] - sorted_values[i] == 1:
            consecutive_values += 1
    if consecutive_values == len(sorted_values)-1:
        all_sequences_consecutive_values.append('cool')
    else:
        all_sequences_consecutive_values.append('not cool')

for i in range(0, len(all_sequences)):
    print(f'In the sequence {all_sequences[i]} -> repeating numbers: {all_sequences_repeating_values[i]}, distinct numbers {all_sequences_distinct_values[i]} ({len(all_sequences_distinct_values[i])} distinct numbers), sequence is {all_sequences_consecutive_values[i]}.')