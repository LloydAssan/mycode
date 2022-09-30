#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - Life of Brian guessing game using a while True loop."""

def main():


    turn = 0
    answer = " "

    while turn < 3 and answer != "Brian":
        turn + 1     # increase the round counter by 1
        answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
        if answer == "Brian": # logic to check if user gave correct answer
            print("Correct!")
        elif turn == 3:    # logic to ensure round has not yet reached 3
            print("Sorry, the answer was Brian.")
        else:                 # if answer was wrong
            print("Sorry. Try again!")





main()


