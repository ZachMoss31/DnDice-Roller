#Application driver
from Lib.dicelib import *

def main():
    #Preprocessing...
    print("Enter a number to roll, or {q} to quit and close.")
    choice = ""
    
    #Driving...
    while choice != 'q':
        choice = input("Enter which kind of dice to roll: ")
        if choice.isdigit():
            RollDice(int(choice), 's')
        elif choice.isalpha():
            CheckChoice(choice)
        else:
            print("Invalid input")
            
    print("Exited rolling.")  

if __name__ == "__main__":
    main()