#1. Please write a function named seven_brothers. When the function is called, it should 
# print out the names of the seven brothers in alphabetical order, as in the example 
# below. 
def seven_brothers():
    br = list(['Aapo',
    'Eero',
    'Juhani',
    'Lauri',
    'Simeoni',
    'Timo',
    'Tuomas']
    )
    print(f'brothers: {br}')
    br.sort()
    print(f'brothers sorted: {br}')
    for b in br:
        print(f'{b}')

seven_brothers()


#2. The exercise contains the outline of the function first_character. Please complete
# it so that it prints out the first character of the string it takes as its argument.

def first_character(text):
     first_ch = text[0]
     print(f'{first_ch}')

# testing the function:
if __name__ == "__main__":
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')

#3. Please write a function named mean, which takes three integer arguments. The 
# function should print out the arithmetic mean of the three arguments.
def mean(x, y, z):
    m = (x + y + z)/3
    print(m)

if __name__ == "__main__":
    mean(5, 3, 1)
    mean(10, 1, 1)


#4. Please write a function named print_many_times(text, times), which takes a string and an 
# integer as arguments. The integer argument specifies how many times the string argument 
# should be printed out.
def print_many_times(text, times):
    for i in range(times):
        print(text)

print_many_times("hi", 5)

print()

text = "All Pythons, except one, grow up"
times = 3
print_many_times(text, times)

#5. Please write a function named hash_square(length), which takes an integer argument. The 
# function prints out a square of hash characters, and the argument specifies the length of 
# the side of the square.
def hash_square(length):
    for i in range(length):
        print(f'{"#" * length}')

hash_square(3)
print()
hash_square(5)

#6. Please write a function named chessboard, which prints out a chessboard made out of ones 
# and zeroes. The function takes an integer argument, which specifies the length of the side 
# of the board.
from math import floor

def chessboard(num):
    for i in range(1, (num+1)):
        if i%2 == 1:
            str1 = "10" * floor(num/2)
            str2 = "1" * (num%2)
            print(f'{str1}{str2}')
        else:
            print(f'{"01" * floor(num/2)}{"0" * (num%2)}')

chessboard(3)
print()
chessboard(6)

#7. Please write a function named squared, which takes a string argument and an integer 
# argument, and prints out a square of characters as specified by the examples below.
# from math import floor
# def squared(in_str, num):
#     l = 1
#     rest = ''
#     rest_len = len(rest)
#     while l <= num:
#         full_times = floor( (num - rest_len)/ len(in_str) ) #number of times in_str is used for lind
#         num_endLet = (num - rest_len) % len(in_str) #additional letters required from next in_str
#         rest_len = len(in_str) - num_endLet #number of letters not used of in_str

#         rest = in_str[-rest_len :] #letters remaining from beginning of in_str
#         print(f'full_times: {full_times}, rest: {rest}({rest_len})')
#         l += 1

def squared(in_str, num):
    letters_req = num * num #number of letters required for printing
    concatStr = ''
    while len(concatStr) < letters_req:
        concatStr += in_str
    #print(f'Concat. string: {concatStr}')

    for i in range(num):
        start = i * num
        print(f'{concatStr[start : (start + num)]}')

squared("ab", 3)
print()
squared("aybabtu", 5)