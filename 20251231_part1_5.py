#1. Please write a program which asks the user for an integer number. The program should print out 
 #"Orwell" if the number is exactly 1984, and otherwise do nothing.
num = int(input('Please type in a number: '))
if num == 1984:
    print('Orwell')
# else:
#     print('The number is not 1984!')

#2. Please write a program which asks the user for an integer number. If the number is 
# less than zero, the program should print out the number multiplied by -1. Otherwise 
# the program prints out the number as is.
num = int(input('Please type in a number: '))
absNum = None
if num >= 0:
    absNum = num
else:
    absNum = -1 * num

print('The absolute value of this number is ' + str(absNum))
#print('Original number: ' + str(num) + '\nAbsolute number: ' + str(absNum))

#3. Please write a program which asks for the user's name. If the name is anything but 
# "Jerry", the program then asks for the number of portions and prints out the total 
# cost. The price of a single portion is 5.90.
name = input('Please tell me your name: ')
if name != 'Jerry':
    portions = int(input('How many portions of soup? '))
    print('The total cost is ' + str(portions * 5.90))
else:
    print('Next please!')

#4. Please write a program which asks the user for an integer number. The program 
# should then print out the magnitude of the number according to the following examples.
num = int(input('Please type in a number: '))
if num < 1000:
    print('This number is smaller than 1000')
    if num < 100:
        print('This number is smaller than 100')
        if num < 10:
            print('This number is smaller than 10')
print('Thank you!')

#4. Please write a program which asks the user for two numbers and an operation. If 
# the operation is add, multiply or subtract, the program should calculate and print 
# out the result of the operation with the given numbers. If the user types in anything 
# else, the program should print out nothing.
n1 = input('Number 1: ')
n2 = input('Number 2: ')
op = input('Operation: ')

if(op == 'add'):
    print(n1 + ' + ' + n2 + ' = ' + str(int(n1)+int(n2)))
elif(op == 'multiply'):
    print(n1 + ' * ' + n2 + ' = ' + str(int(n1)*int(n2)))
elif(op == 'subtract'):
    print(n1 + ' - ' + n2 + ' = ' + str(int(n1)-int(n2)))

#5. Please write a program which asks the user for a temperature in degrees Fahrenheit, 
# and then prints out the same in degrees Celsius. If the converted temperature falls 
# below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".
T_F = int(input('Please type in a temperature (F): '))
T_C = (T_F - 32) * 5/9

print(f'{T_F} degrees Fahrenheit equals {T_C} degrees Celsius')
if T_C < 0:
    print("Brr! It's cold in here!")

#6. Please write a program which asks for the hourly wage, hours worked, and the day 
# of the week. The program should then print out the daily wages, which equal hourly 
# wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.
hourly_wage = float(input('Hourly wage: '))
hours_worked = float(input('Hours worked: '))
DoW = input('Day of the week: ')

if DoW == 'Sunday':
    print(f'Daily wages: {2 * hourly_wage * hours_worked} euros')
else:
    print(f'Daily wages: {hourly_wage * hours_worked} euros')

#6. This program calculates the end of year bonus a customer receives on their loyalty 
# card. The bonus is calculated with the following formula:
# If there are less than a hundred points on the card, the bonus is 10 %
# In any other case the bonus is 15 %

points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
elif points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")

#7. Please write a program which asks for tomorrow's weather forecast and then suggests 
# weather-appropriate clothing.
# The suggestion should change if the temperature (measured in degrees Celsius) is over 
# 20, 10 or 5 degrees, and also if there is rain on the radar.
print('What is the weather forecast for tomorrow?')
T = float(input('Temperature: '))
rain = input('Will it rain (yes/no): ')

print('Wear jeans and a T-shirt')
if(T <= 20):
    print('I recommend a jumper as well')
if(T <= 10):
    print('Take a jacket with you')
if(T <= 5):
    print('Make it a warm coat, actually\nI think gloves are in order')
if(rain == 'yes'):
    print("Don't forget your umbrella!")

#8. Please write a program for solving a quadratic equation of the form ax²+bx+c. 
# The program asks for values a, b and c. It should then use the quadratic formula 
# to solve the equation. The quadratic formula expressed with the Python sqrt 
# function is as follows:
# x = (-b ± sqrt(b²-4ac))/(2a).
# You can assume the equation will always have two real roots, so the above formula 
# will always work.

from math import sqrt

a = int(input('Value of a: '))
b = int(input('Value of b: '))
c = int(input('Value of c: '))

root1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
root2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
print(f'The roots are {root1} and {root2}')