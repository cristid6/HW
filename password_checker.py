#O functie ce verifica daca o parola respecta cerintele:
#Sa aibe cel putin un numar, sa aibe cel putin un caracter special,
#sa aibe o cel putin o litera mare si sa fie de cel putin dimensiune 8

#Exemplu:
#Input : R@m@_f0rtu9e$
#Output : Valid Password

#Input : Ramafortune$
#Output : Invalid Password
#Explanation: Number is missing

#Input : Rama#fortu9e
#Output : Invalid Password
#Explanation: Must consist from  or @ or $

password = input('Please enter a password to check it:')

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'X']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

if len(password) >= 8:
    if ' ' not in password:
        number_checker = 0
        upper_letter_checker = 0
        lower_letter_checker = 0
        for character in password:
            if character in numbers:
                number_checker += 1
            if character in upper_letters:
                upper_letter_checker += 1
            if character in lower_letters:
                lower_letter_checker += 1
        if number_checker + upper_letter_checker + lower_letter_checker < len(password) and number_checker > 0 and upper_letter_checker > 0:
            print('Valid password!')
        elif number_checker == 0:
            print('Invalid password! Explanation: Number is missing!')
        elif upper_letter_checker == 0:
            print('Invalid password! Explanation: Uppercase is missing!')
        else:
            print('Invalid password! Explanation: Special character is missing!')
    else:
        print('Invalid password! Explanation: Space character in password!')
else:
    print('Invalid password! Explanation: Minimum length 8 characters!')

