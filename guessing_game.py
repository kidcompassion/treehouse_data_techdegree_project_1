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


def start_game(current_game_counter, username):
    """
    Create the start_game function.

    Args:
    current_game_counter: tells us how many times the user has played
    username: tells us the user's name

    """

    # This will hold all guesses for the current game
    list_of_guesses = []
    
    #   1. Display an intro/welcome message to the player.
    print("\n=======>", "WELCOME TO THE NUMBER GUESSING GAME!"," <=======\n")
    
    # Check the current game counter to see if the user has played before.
    # If the counter is 0, it means they haven't and can share their name.
    
    if current_game_counter == 0:
        username = str(input("Please enter your name: \n"))

    # Users can enter any name containing any type of character,
    # it just can't be empty. Keep prompting them until they add something.
    while username == "":
        username = str(input("You cannot leave this empty. Please enter your name: \n"))
    
    #   2. Store a random number as the answer/solution.
    generated_num = random.randint(1, 10)

    # Increment counter, now that the game is starting.
    current_game_counter += 1

    #remove this later
    print(f"Number is {generated_num}")
    # Get the user's first guess
    print(f"Good luck, {username}! I’ve generated a secret number for you to guess.\n")
    
    # Initial user guess
    # In order to show a unique message on the first guess, set a loop
    # to keep running until a valid guess is entered.
    while True:
        try:
            guess = int(input(f"What do you think the secret number is? \n"))
            # If the guess is too high or too low, tell the user
            if guess > generated_num:
                print("Too high!")
            elif guess < generated_num:
                print("Too low!")
            # then break out of this loop so we can update the error messaging
            break
        except ValueError:
            print("****", "I'm sorry, that's not a valid guess! Please enter an integer between 1 and 10. \n")
          
    # Once the guess is valid, add it to our list
    list_of_guesses.append(guess)

    #   3. Continuously prompt the player for a guess.
    while guess != generated_num:
        try:
            # Now, give the user a prompt for the rest of their attempts
            guess = int(input("Go again: "))
            list_of_guesses.append(guess)
            # If the guess is a number, give the user some feedback

            # 3b. If the guess is less than the solution, display to the player "It's higher".
            if guess > generated_num:
                print("Too high!")
            # 3a. If the guess is greater than the solution, display to the player "It's lower".
            elif guess < generated_num:
                print("Too low!")
        except ValueError:
            print("Please enter an integer between 1 and 10")


    #   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
    print(list_of_guesses)
    print(f"You got it, {username}! Great job!\n")
    print(f"|************* YOUR STATS **************|\n")
    print(f"This was game {current_game_counter}")
    #5a. How many attempts it took them to get the correct number in this game
    print(f"You guessed {len(list_of_guesses)} times to get it right.")
    #5b. The mean of the saved attempts list
    print(f"Your median guess was {statistics.median(list_of_guesses)}")
    #5c. The median of the saved attempts list
    print(f"Your mean guess was {statistics.mean(list_of_guesses)}")
    #5d. The mode of the saved attempts list
    print(f"Your mode guess was {statistics.mode(list_of_guesses)}\n")
    #   6. Prompt the player to play again
    winning_response = input(f"Would you like to play again? Enter Y or N. \n")
    # 6a. If they decide to play again, start the game loop over.
    if winning_response.lower() == 'y':
        start_game(current_game_counter, username)
    else:
        # 6b. If they decide to quit, show them a goodbye message.
        print(f"Okay, {username}! Great work and we'll see you later.")
        sys.exit()
 
# Kick off the program by calling the start_game function.
start_game(current_game_num, username)