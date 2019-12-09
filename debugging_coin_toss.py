#! python3
# debugging_coin_toss.py - given file supposed to help train debugging
# Usage: python.exe debugging_coin_toss.py
# 09-12-2019 elective skill

import random

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == 1:
    toss = 'heads'
else:
    toss = 'tailss'

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    while True:
        guess = input()
        if guess in ('heads', 'tails'):
            break
        print('Enter heads or tails:')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
