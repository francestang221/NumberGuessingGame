"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():
    # Welcome message
    print("-" * 39 + "\n Welcome to the Number Guessing Game! \n" + "-" * 39)

    game_on = True
    game_round = 0
    high_score = None
    guess_counter = 1
    num_rand = random.randint(1, 10)

    while game_on:
        try:
            print("\n" + ">" * 5 + " ATTEMPT {} ".format(guess_counter) + "<" * 5)
            num_guess = int(input("\nPick a number between 1 and 10: "))

            if num_guess != num_rand:
                if num_guess > 10 or num_guess < 1:
                    guess_counter += 1
                    print("\nYour guess was out of range. Please pick a number between 1 and 10. ")

                elif num_guess > num_rand:
                    print("\nIt's lower. Try again.")
                    guess_counter += 1
                elif num_guess < num_rand:
                    print("\nIt's higher. Try again.")
                    guess_counter += 1
                    continue

            elif num_guess == num_rand:
                print("\n WOO-HOO! You got it! It took you {} tries. ".format(guess_counter))
                game_round += 1
                if game_round == 1:
                    high_score = guess_counter

                if game_round > 1:
                    if guess_counter < high_score:
                        high_score = guess_counter

                try_again = input("\nOne more round? press 'y' to continue, or any other key to quit: ").lower()

                if try_again == 'y':
                    print("\nYOUR BEST RECORD IS {} TRIES ".format(high_score))
                    guess_counter = 1
                    game_round += 1
                    num_rand = random.randint(1, 10)
                    continue

                else:
                    print("\n Closing game...see you next time! ")
                    game_on = False

        except ValueError:
            print("\n Oops! That was not a valid guess. Please enter a number.")
            guess_counter += 1


# Kick off the program by calling the start_game function

start_game()