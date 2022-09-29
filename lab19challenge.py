#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - Challenge - Lesson 19"""

import random


def main():
    # variable with list
    wordbank = ["indentation", "spaces"]
    
    # variable with list named tlgstudents
    tlgstudents= ["Aaron", "Lloyd", "Asif", "Brent",
                    "Cedric", "Chris", "Cory", "Ebrima",
                    "Franco", "Greg", "Hoon", "Joey",
                    "Jordan", "JC", "LB", "Mabel",
                    "Shon", "Pat", "Zach"]
    print(tlgstudents)


    # line of code that appends integer 4 into the list world bank
    wordbank.append(4)
    print(wordbank)

     # input change to integer
    num = int(input("Enter a number between 0 and 18 here: "))
    print(num)
    name = tlgstudents[num]

    print(f"Your unfortunate victim is {name}!")
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent")

main()

