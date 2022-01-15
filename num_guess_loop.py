# Created by: Navin Balekomebole
# Created on: Jan 15, 2022
# This program will ask the user to guess a number
# between 0 and 9 and tells them if it is correct.
# It loops the program if it is incorrect.
import random


def main():
    # set the correct number
    correct = random.randint(0, 9)

    # loop
    while True:
        # get user’s number
        user_string = input("Enter your number: ")

        # error checking
        try:
            user_number = int(user_string)
        except Exception:
            print("invalid input")
        else:
            # check number size
            if user_number >= 10:
                print("Number must be between 0 and 9.")

            elif user_number <= -1:
                print("Number must be between 0 and 9.")

            # if correct
            elif user_number == correct:
                print("You are Correct!")
                break

            else:
                print("Sorry but you are Incorrect")


if __name__ == "__main__":
    main()