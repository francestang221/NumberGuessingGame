"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():
    # Welcome message
    print("-" * 39 + "\n Welcome to the Number Guessing Game! \n" + "-" * 39)

    try:
        high_score = 10
        guess_msg = "Pick a number between 1 and 10: "
        guess_counter = 1

        while guess_counter > 0:
            num_rand = random.randint(1, 10)
            num_guess = int(input(guess_msg))
            if num_guess > 10 or num_guess < 1:
                raise ValueError("Your guess is out of range. Please pick a number between 1 and 10 next time.")

            guess_counter = 1
            while num_guess != num_rand:
                if num_guess > num_rand:
                    print("It's lower")
                    num_guess = int(input(guess_msg))
                    if num_guess > 10 or num_guess < 1:
                        raise ValueError("Your guess is out of range. Please pick a number between 1 and 10 next time.")

                elif num_guess < num_rand:
                    print("It's higher")
                    num_guess = int(input(guess_msg))
                    if num_guess > 10 or num_guess < 1:
                        raise ValueError("Your guess is out of range. Please pick a number between 1 and 10 next time.")
                guess_counter += 1

                if num_guess == num_rand:
                    print("You got it! It took you {} tries. ".format(guess_counter))
                high_score = guess_counter
                if guess_counter > 1:
                    if high_score > guess_counter:
                        high_score = guess_counter
            try_again = input("Would you like to try again?  [y]es/[n]o: ")

            if try_again == 'y':
                print("the HIGHSCORE IS {} ".format(high_score))
                continue
            else:
                print("Closing game...see you next time! ")
                break

    except ValueError as err:
        print("Invalid Value. Try again!")
        print("({}) ".format(err))


# Kick off the program by calling the start_game function

start_game()