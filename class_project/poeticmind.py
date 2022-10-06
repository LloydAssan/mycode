#!/usr/bin/env python3

""" Author: Lloyd Assan || Python Final Project
    || Project takes in user name and randomly returns one of ten poems store in txt"""


import random

def main():

    # user input - name
    user = input('Enter your name: ')
    print('=======================================================================================')
    user = print(f" {user}, you are welcome to the poetic mind space.")
    print('=======================================================================================')



    # Open the file in read mode
    count = random.randint(1, 10)
    with open(f'poem{count}.txt', "r") as poem:
        read_poem = poem.read()
    print(read_poem)

if __name__ == "__main__":
    main()