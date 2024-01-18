#Program to roll a random dice of a certain number in DnD.
import random

#Function to roll random dice dependent on dice roll
def RollDice(num, rollType):
#Preprocessing...
    #Is our choice a valid dice?
    if num not in {4,6,8,10,12,20}:
        print("Num is not a valid dice.")
        return 0
    #Set rollType to lower for ease of use
    rollType = rollType.lower()

#Driving...
    #Standard Roll
    if rollType == 's':
        roll = random.randint(1, num)
        
    
    #Advantaged Roll    
    elif rollType == 'a':
        print("\nRolling advantage...")
        roll1 = random.randint(1,num)
        roll2 = random.randint(1,num)
        roll = roll1 if roll1 > roll2 else roll2
        
    #Disadvantaged Roll
    elif rollType == 'd':
        print("\nRolling disadvantage...")
        roll1 = random.randint(1,num)
        roll2 = random.randint(1,num)
        roll = roll1 if roll1 < roll2 else roll2
        
    print("You rolled ", roll)
    return roll

#Function to roll random dice and sum the result
def SumDice():
    #Catching invalid inputs
    num = input("Enter dice type: ")
    while num.isdigit() == False:
        print("Invalid input")
        num = input("Enter dice type: ")
    
    numRolls = input("Enter num rolls: ")
    while numRolls.isdigit() == False:
        print("Invalid input")
        numRolls = input("Enter num rolls: ")
        
    num = int(num)
    numRolls = int(numRolls)
    
    #Catching invalid dice choices
    if num not in {4,6,8,10,12,20}:
        print("Num is not a valid dice.")
        return
        
    sum = 0
    for x in range(numRolls):
        sum += RollDice(num, 's')
    print("Total: ", sum)

#Function to determine advantage, disadvantage, or roll a sum of dice.
def CheckChoice(option):
    option = option.lower()
    options = {'a','d','n','q'}
    if option not in options:
        print("Invalid input")
        return
    
    if option == 'q':
        return
    elif option == 'a':
        RollDice(20, 'a')
    elif option == 'd':
        RollDice(20, 'd')
    elif option == 'n':
        SumDice()