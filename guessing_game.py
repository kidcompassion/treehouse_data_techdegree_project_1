"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import random
import sys
import statistics


# this will tell us how many times user has played
current_game_num = 0
# This will remember user's name
username = ""
# This will keep track of scores across across all games
list_of_scores = []


def start_game(current_game_counter, username):
    """
    Create the start_game function.

    Args:
    current_game_counter: tells us how many times the user has played
    username: tells us the user's name

    """

    # List of guesses (for the current name only)
    list_of_guesses = []
    
    #Display an intro/welcome message to the player.
    print("\n=======>", "WELCOME TO THE NUMBER GUESSING GAME!"," <=======\n")
    
    # Check the current game counter to see if the user has played before.
    # If not, ask for their name 
    if current_game_counter == 0:
        username = str(input("Please enter your name: "))
    # If so, show their high score
    else:
        print(f"***Can you beat your best ever score of just {min(list_of_scores)} guesses?***\n")

    # If a username hasn't been set, ask them to enter one
    while username == "":
        username = str(input("You cannot leave this empty. Please enter your name: "))
    
    # Store a random number as the answer/solution.
    generated_num = random.randint(1, 10)

    # Keep track of how many games have been played
    current_game_counter += 1

    # Get the user's first guess
    print(f"\nGood luck, {username}! I’ve generated a secret number between 1 and 10 for you to guess.\n")
    
    # Initial user guess
    # In order to show a unique message on the first guess, set a loop
    # to keep running until a valid guess is entered.
    while True:
        try:
            guess = int(input(f"What do you think the secret number is? \n"))
            
            # * Check if the first guess is in the range of 1 - 10
            # * If not, show an error
            if guess in range(1, 10):
                # If the guess is valid, but too high or too low, tell the user
                if guess > generated_num:
                    print("Too high!")
                elif guess < generated_num:
                    print("Too low!")
                else:
                     # Once the guess from the first try is valid, add it to our list
                    list_of_guesses.append(guess)
                # then break out of this loop so we can update the error messaging
                break
            else:
                print("You guessed a number outside of 1 - 10. Try again.")
        except ValueError:
            print("I'm sorry, that's not a valid guess! Please enter an integer between 1 and 10.")

    #  3. Continuously prompt the player for a guess.
    #  Loop will break once the guess is the same as the generated number
    while guess != generated_num:
        try:
            # Now, give the user a prompt for the rest of their attempts
            guess = int(input("Go again: "))
            
            # If the guess is valid, give the user some feedback
            if guess in range(1, 10):
                # 3b. If the guess is less than the solution, display to the player "It's higher".
                if guess > generated_num:
                    print("Too high!")
                # 3a. If the guess is greater than the solution, display to the player "It's lower".
                elif guess < generated_num:
                    print("Too low!")
                # If the guess is valid, add it in total number of guesses
                list_of_guesses.append(guess)
            else:
                print("You guessed a number outside of 1 - 10. Try again.")
        except ValueError:
            print("Please enter an integer between 1 and 10")


    # Add the total number of guesses from this game to use as a score
    list_of_scores.append(len(list_of_guesses))
    
    #   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
    print(f"You got it, {username}! Great job!\n")

    print(f"|===============> YOUR STATS <===============|\n")
    # Tell them how many games they've played
    print(f"This was game #{current_game_counter}")
    # Just for fun, tell them the average number of guesses they have used across all games
    # 5a. How many attempts it took them to get the correct number in this game
    print(f"* This time, you guessed {len(list_of_guesses)} times to get the answer.")
    # 5b. The mean of the saved attempts list
    print(f"* Your median number of guesses across all games is {round(statistics.median(list_of_scores))}")
    # 5c. The median of the saved attempts list
    print(f"* Your mean (average) number of guesses across all games is {round(statistics.mean(list_of_scores))}")
    # 5d. The mode of the saved attempts list
    print(f"* Your mode (most frequently occurring number of guesses) across all games is {statistics.mode(list_of_scores)}\n")


    #6. Prompt the player to play again
    winning_response = input(f"Would you like to play again? Enter Y or N. \n")
    #6a. If they decide to play again, start the game loop over.
    if winning_response.lower() == 'y':
        start_game(current_game_counter, username)
    else:
        # 6b. If they decide to quit, show them a goodbye message.
        print(f"Okay, {username}! Great work and we'll see you later.")
        sys.exit()
 
# Kick off the program by calling the start_game function.
start_game(current_game_num, username)