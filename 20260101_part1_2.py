#1. Please write a program which asks for the user's name and then prints it twice, on two 
# consecutive lines.

name = input('What is your name? ')
print(f'{name}\n{name}')

#2. Please write a program which asks for the user's name and then prints it out twice on a 
# single line so that there is an exclamation mark at the beginning of the line, another between 
# the two names and a third one at the end of the line.
name = input('What is your name? ')
print(f'!{name}!{name}!')

#3. Please write a program which asks for the user's name and address. The program should also 
# print out the given information, as follows:
# Given name: Steve
# Family name: Sanders
# Street address: 91 Station Road
# City and postal code: London EC05 6AW
# Steve Sanders
# 91 Station Road
# London EC05 6AW

givenName = input('Given name: ')
familyName = input('Family name: ')
streetAd = input('Street address: ')
city_PC = input('City and postal code: ')

print(f'{givenName} {familyName}\n{streetAd}\n{city_PC}')

#4. Here is a program which should ask for three utterances and print them out, like so:
# The 1st part: hickory
# The 2nd part: dickory
# The 3rd part: dock
# hickory-dickory-dock!

# Fix the code
part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(part1 + '-' + part2 + '-' + part3 + '!')

#5. Please write a program which prints out the following story. The user gives a name and a 
# year, which should be inserted into the printout.
# Please type in a name: Mary
# Please type in a year: 1572

# Mary is a valiant knight, born in the year 1572. One morning Mary woke up to an awful racket: 
# a dragon was approaching the village. Only Mary could save the village's residents.

n = input('Please type in a name: ')
y = input('Please type in a year: ')
print(n + ' is a valiant knight, born in the year ' + y +
    '. One morning ' + n + ' woke up to an awful racket: a dragon was approaching the village.' +
    ' Only ' + n + " could save the village's residents.")