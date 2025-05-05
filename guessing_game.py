"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
import sys
import statistics


# Create the start_game function.

def start_game():
    # This will hold all guesses
    list_of_guesses = []
    # Welcome the user
    print("|******** Welcome to the number guessing game! *********|\n")
    
    # For fun, ask their name
    username = str(input("Please enter your name: "))
    
    # Users can enter any name they want, but it has to be something.
    # While the username is empty, keep prompting them to put their name.
    while username == "":
        username = str(input("You cannot leave this empty. Please enter your name: "))
    
    # Choose a random number
    generated_num = random.randint(1, 11)

    



    #remove this later
    print(f"Number is {generated_num}")
    
    # Get the user's guess
    # add error handling
    
    try:
        guess = int(input(f"Hi {username}! I’ve just generated a number for you to guess. What do you think it is?"))
    except ValueError:
        print("This is a value error")
    
    
    
    #add the guess to the list
    list_of_guesses.append(guess)

    # until the guess matches the number, keep guessing
    while guess != generated_num:
        if guess> generated_num:
            # if this is higher, alert the user
            guess = int(input(f"Good guess, but that was too high. Guess again: "))
            list_of_guesses.append(guess)

        elif guess < generated_num:
            #if this is lower
            guess = int(input(f"So close! But that was too low. Guess again: "))
            list_of_guesses.append(guess)
        

    print(list_of_guesses)
    
    print(f"You did it, {username}! Great job!")
    print(f"You guessed {len(list_of_guesses)} times")
    print(f"Your median guess was {statistics.median(list_of_guesses)}")
    print(f"Your mean guess was {statistics.mean(list_of_guesses)}")
    print(f"Your mode guess was {statistics.mode(list_of_guesses)}")
    
    winning_response = input(f"Would you like to play again? Enter Y or N. \n")

    if winning_response.lower() == 'y':
        start_game()
    else:
        print(f"Okay, {username}! Great work and we'll see you later.")
        sys.exit()
    
# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
#   5. Display the following data to the player
#     a. How many attempts it took them to get the correct number in this game
#     b. The mean of the saved attempts list
#     c. The median of the saved attempts list
#     d. The mode of the saved attempts list
#   6. Prompt the player to play again
#     a. If they decide to play again, start the game loop over.
#     b. If they decide to quit, show them a goodbye message.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
start_game()