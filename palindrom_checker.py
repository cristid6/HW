#The palindrom checker:
#Creati o functie ce verifica daca un sir de caractere este un palindrom sau nu
#ex:
#Input: aba
#Output: YES

possible_palindrom = input('Insert one word to check if it\'s a palindrom:')
check_palindrom = possible_palindrom[::-1]
if possible_palindrom == check_palindrom:
    print('YES')
else:
    print('NO')