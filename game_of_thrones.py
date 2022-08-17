#Game of Thrones
#Dothraki plănuiesc să usurpe tronul Regelui Robert. Regele Robert aude de această conspirație de la un raven și plănuiește să încuie singura ușă prin care inamicul poate să pătrundă în regat lui.
#    Dar această ușă are nevoie de o cheie care este reprezentată de către anagrama unui palindrom. începe să caute în cutia lui de șiruri de caractere, verificând pe fiecare în parte dacă poate fi rearanjat într-un palindrom.
#Cerință:
#    Pentru un șir de caractere, să se tipărească pe ecran cuvântul DA sau NU dacă acest șir poate fi rearanjat astfel încât să fie un palindrom.
#Constrangeri:
#Pot fi folosite doar caractere din alfabetul latin cu litere mici
#Date de intrare:
#   Șirul de caractere.
#Exemplu:
#INPUT:
#aaabbbb
#OUTPUT:
#DA
#Șirul poate fi permutat astfel: bbaaabb

while True:

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                        'v', 'w', 'x', 'y', 'z']

    my_string = input('Please enter a string to check if it can be a palindrom:')

    for character in my_string:
        if character not in letters:
            print('Please enter only latin lower letter!')
            break

    counter_list = []
    letter_list = []

    for letter in letters:
        counter = 0
        if letter in my_string:
            for character in my_string:
                if character == letter:
                    counter += 1
            counter_list.append(counter)
            letter_list.append(letter)

    odd_numbers = 0

    for counter in counter_list:
        if counter % 2 == 1:
            odd_numbers += 1

    if odd_numbers > 1:
        print('NO')
    elif odd_numbers == 0:
        palindrom = ''
        palindrom_element_list = []
        for i in range(0,len(letter_list)):
            element = letter_list[i] * counter_list[i]
            palindrom_element_list.append(element)
        if len(palindrom_element_list) == 1:
            palindrom = palindrom_element_list[0]
            print(f'YES. The palindrom can look like this: {palindrom}')
        else:
            for i in range(0,len(palindrom_element_list)):
                palindrom += palindrom_element_list[i][:int(len(palindrom_element_list[i])/2)]
            palindrom += palindrom[::-1]
            print(f'YES. The palindrom can look like this: {palindrom}')
    else:
        palindrom = ''
        palindrom_element_list = []
        for i in range(0,len(letter_list)):
            element = letter_list[i] * counter_list[i]
            palindrom_element_list.append(element)
        if len(palindrom_element_list) == 1:
            palindrom = palindrom_element_list[0]
            print(f'YES. The palindrom can look like this: {palindrom}')
        else:
            for i in range(0,len(palindrom_element_list)):
                palindrom += palindrom_element_list[i][:int(len(palindrom_element_list[i])/2)]
            odd_letter = ''
            for counter in counter_list:
                if counter % 2 == 1:
                    odd_letter = letter_list[counter_list.index(counter)] * (counter)
            if len(odd_letter) == 1:
                palindrom += odd_letter[0:len(odd_letter)] + palindrom[::-1]
                print(f'YES. The palindrom can look like this: {palindrom}')
            else:
                palindrom += odd_letter[0:1] + palindrom[::-1]
                print(f'YES. The palindrom can look like this: {palindrom}')


