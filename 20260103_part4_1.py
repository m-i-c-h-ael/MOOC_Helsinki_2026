#1. Please write a program which asks the user which editor they are using. The program should 
# keep on asking until the user types in Visual Studio Code.
#If the user types in Word or Notepad, the program counters with awful. Other unacceptable editor choices receive the reply not good.
#The program should be case-insensitive in its reactions. That is, the same user input in 
# lowercase, uppercase or mixed case should trigger the same reaction:
while True:
    editor = input('Editor: ').lower()
    if editor == 'visual studio code':
        print('an excellent choice!')
        break
    elif editor == 'word' or editor == 'notepad':
        print('awful')
    else:
        print('not good')