import random

def compare_numbers(number, user_guess):
    ## your code here
    COW=0 #assigned as 0 initially because the program can add it against the variable that comes in the loop, in order to recieve wrong guess
    BULL=0 #assigned as 0 initially because the program can add it against the variable that comes in the loop, in order to recieve correct guess

    for x in range(4): #loop to check each digit

        if user_guess[x] == number[x]: # checks if the guess is right
            BULL = BULL + 1 

        else: # checks if the guess is wrong
            COW = COW + 1
            
    cowbull =[COW,BULL]  #store these values to a list so that they can futher be accessed by its index position  
    return cowbull

playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
guesses = 0
print (number)

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
