# 1. Your friend is working on an app for jobseekers. She sends you this bit of code:

# name = "Tim Tester"
# age = 20
# skill1 = "python"
# level1 = "beginner"
# skill2 = "java"
# level2 = "veteran"
# skill3 = "programming"
# level3 = "semiprofessional"
# lower = 2000
# upper = 3000

# print("my name is ", name, " , I am ", age, "years old")
# print("my skills are")
# print("- ", skill1, " (", level1, ")")
# print("- ", skill2, " (", level2, ")")
# print("- ", skill3, " (", level3, " )")
# print("I am looking for a job with a salary of", lower, "-", upper, "euros per month")

# The program should print out exactly the following:

# my name is Tim Tester, I am 20 years old

# my skills are
#  - python (beginner)
#  - java (veteran)
#  - programming (semiprofessional)

# I am looking for a job with a salary of 2000-3000 euros per month

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old\n")
print(f"my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})")
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

#2. his program already contains two integer variables, x and y:
# x = 27
# y = 15
# Please complete the program so that it also prints out the following:

# 27 + 15 = 42
# 27 - 15 = 12
# 27 * 15 = 405
# 27 / 15 = 1.8

# The program should work correctly even if the values of the variables are changed. That is, if the first two lines are replaced with this

# x = 4
# y = 9
# the program should print out the following:

# Sample output
# 4 + 9 = 13
# 4 - 9 = -5
# 4 * 9 = 36
# 4 / 9 = 0.4444444444444444

x = 4 #27
y = 9 #15

print(f'{x} + {y} = {x+y}')
print(f'{x} - {y} = {x-y}')
print(f'{x} * {y} = {x*y}')
print(f'{x} / {y} = {x/y}')