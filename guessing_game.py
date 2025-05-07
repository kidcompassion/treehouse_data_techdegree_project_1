"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
import sys
import statistics


current_game_num = 0
username = ""

# 
# Give it 
def start_game(current_game_counter, username):
    """
    Create the start_game function.

    Args:
    current_game_counter: tells us how many times the user has played
    username: tells us the user's name

    """


    # This will hold all guesses for the current game
    list_of_guesses = []
    
    # Welcome the user
    print("\n=======>", "WELCOME TO THE NUMBER GUESSING GAME!"," <=======\n")

    
    # Check the current game counter to see if the user has played before.
    # If the counter is 0, it means they haven't and can share their name.
    
    if current_game_counter == 0:
        username = str(input("Please enter your name: \n"))
    
    
    # Users can enter any name containing any type of character,
    # it just can't be empty. Keep prompting them until they add something.
    
    while username == "":
        username = str(input("You cannot leave this empty. Please enter your name: \n"))
    
    # Choose a random number from 1-10 for user to guess
    generated_num = random.randint(1, 10)

    # Increment counter, now that the game is starting.
    current_game_counter += 1

    #remove this later
    print(f"Number is {generated_num}")
    # Get the user's first guess


    # Set a switch to ensure any errors get re-tried
    
    print(f"Good luck, {username}! I’ve generated a secret number for you to guess.\n")
    
    # While the switch is set to false, keep looping
    while True:
        try:
            #Let the user guess. If the guess is valid, set the switch to True to break out of the loop.
            guess = int(input(f"What do you think the secret number is? \n"))
            if guess > generated_num:
                print("Too high!")
            elif guess < generated_num:
                print("Too low!")
            break
        except ValueError:
            print("****", "I'm sorry, that's not a valid guess! Please enter an integer between 1 and 10. \n")
        
    
    # once the guess is valid, add it to our list
    list_of_guesses.append(guess)
   
    while guess != generated_num:
        
        
            
        
        try:    
            guess = int(input("Go again: "))
            list_of_guesses.append(guess)
            # If the guess is a number, give the user some feedback
            if guess > generated_num:
                print("Too high!")
            elif guess < generated_num:
                print("Too low!")

        except ValueError:
            print("Please enter an integer between 1 and 10")



    print(list_of_guesses)
    print(f"You did it, {username}! Great job!\n")
    print(f"|************* YOUR STATS **************|\n")
    print(f"This was game {current_game_counter}")
    print(f"You guessed {len(list_of_guesses)} times to get it right.")
    print(f"Your median guess was {statistics.median(list_of_guesses)}")
    print(f"Your mean guess was {statistics.mean(list_of_guesses)}")
    print(f"Your mode guess was {statistics.mode(list_of_guesses)}\n")
    
    winning_response = input(f"Would you like to play again? Enter Y or N. \n")

    if winning_response.lower() == 'y':
        start_game(current_game_counter, username)
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
start_game(current_game_num, username)