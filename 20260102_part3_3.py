#1. Please write a program which asks the user for a positive integer number. The 
# program then prints out a list of multiplication operations until both operands reach 
# the number given by the user.
numb = int(input('Please type in a number: '))
for i in range(1, numb +1):
    for j in range (1, numb + 1):
        print(f'{i} x {j} = {i*j}')

#2. Please write a program which asks the user to type in a sentence. The program then 
# prints out the first letter of each word in the sentence, each letter on a separate 
# line.
sent = input('Please type in a sentence: ')
words = sent.split(' ')
for w in words:
    print(f'{w[0]}')

#3. Please write a program which asks the user to type in an integer number. If the 
# user types in a number equal to or below 0, the execution ends. Otherwise the program 
# prints out the factorial of the number.
while True:
    num = int(input('Please type in a number: '))
    if num > 0:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print(f'The factorial of the number {num} is {fact}')
    else:
        print('Thanks and bye!')
        break

#4. Please write a program which asks the user to type in a number. The program then
# prints out all the positive integer values from 1 up to the number. However, the 
# order of the numbers is changed so that each pair or numbers is flipped. That is, 
# 2 comes before 1, 4 before 3 and so forth. See the examples below for details.
num = int(input('Please type in a number: '))
i = 1
while i+1 <= num:
    print(f'{i+1}\n{i}')
    i += 2
if i == num:
    print(f'{i}')

#5. Please write a program which asks the user to type in a number. The program then 
# prints out the positive integers between 1 and the number itself, alternating between 
# the two ends of the range as in the examples below.
num = int(input('Pleast type in a number: '))
i = 0
if not type(num) == 'int' or not num >= 1:
    exit
while i != num:
    i += 1
    print(i)
    if i < num:
        print(num)
        num -= 1