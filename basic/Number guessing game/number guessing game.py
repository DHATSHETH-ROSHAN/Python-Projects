import random         # inporting random module to generate the random values between the given values
import math           # importing the math module to use the mathematical operations


def progress_bar(guess,chances):    # making the progress bar function 
    progress = int((guess/chances)*20)  
    bar = '🪦' * progress + '❤️' * (20 - progress)
    print(f"[{bar}] {guess}/{chances} chances used")

def chance(lb,ub):                  # calculating the correct number of chances for the given lowerr bound  to upper bound
    range_size = ub - lb + 1
    ch = math.ceil(math.log2(range_size))
    return ch

print("HI, Welcome to the number guessing game.")


while True:           # making the program to run repetedly untill the person finishes the game and exits the game 
    lb = int(input("Enter the lower bound value: "))
    ub = int(input("Enter the upper bound value: "))
    
    chances = chance(lb, ub)
    print("your maximum no of chances is: ", chances)
    val = random.randrange(lb,ub)
    
    guess = 0
    
    while guess < chances:      # no making the player to guess untill he lose his chances
        guess += 1
        progress_bar(guess, chances)
        
        gt = int(input("Enter your guess value: "))
        
        
        if guess == 2:      # giving hint to the player 
            print(f"Hint: The number is {'even' if val % 2 == 0 else 'odd'}.")
        
        
        
        if guess >= chances and gt != val:    # Diplaying the output to the user that he failed
            print(f'Oops sorry, better luck next time, The number was {val}')
        elif gt == val:                     # if the user prredicts correctly then it needs to be displaed as guessed correctly
            print( f'The number is {val} and your guess it correct. you found it in {guess} attempt')
            break
        elif gt > val:                      
            print('Your guess is higher dude!!😢')
        elif gt < val:
            print('your guess is lower than what i gave you!! 😂 ')
    
    
    
    replay = input("Do you want to play again? (yes/no): ").strip().lower()   # getting know that the user wants to play or not
    if replay != "yes":     # if the user enters anything other than yes then the game ends
        print("Thanks for playing! Goodbye!")
        break