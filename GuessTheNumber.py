# Guess the number game (user)
import random
import sys
print('GUESS THE NUMBER GAME'.center(10))
print("Welcome player! \n"
      "Would you like to play?. yes or no.")


def guess_number_game():
    answer = input().lower()
    while answer != "yes" and answer != 'no':
        print("Enter yes or no")
        answer = input().lower()
    if answer == 'yes':
        print("let's go! ")
    else:
        if answer == 'no':
            print("Bye!")
            sys.exit()

    guesses = 0
    secret_number = random.randint(1, 20)
    print("Guess a number between 1-20!")
    while True:
        guessed_num = int(input())

        if guessed_num < secret_number:
            print("Your guess is too low")
        else:
            if guessed_num > secret_number:
                print("Your guess is too high.")

        if guessed_num != secret_number:
            guesses += 1
            if guesses == 5:
                print("YOU FAILED \nThe secret number was "
                      + str(secret_number))
                print("Would you like to play again")
                guess_number_game()

            print("Try again")
        else:
            if guessed_num == secret_number:
                print("YOU WON! \nYou guessed the secret number in "
                      + str(guesses + 1) + ' guesses')
                print('Would you like to play again')
                guess_number_game()


guess_number_game()

