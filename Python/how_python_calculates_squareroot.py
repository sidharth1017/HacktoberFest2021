"""
Ever wondered how python is able to calculate squareroot of a non-perfect square number?
This code shows how is python able to calculate it !

Code contributed by: Hriday Agrawal
Github Name: HridayAg0102


#======SAMPLE OUTPUT:=========#

Number: 300143838031, its root: 547853.8473270038

Start approximation
650072.8960528814
555890.4336743704
547911.940357758
547853.850406696
547853.8473270038
Found true root after 6 guesses.
"""


import random

# get a random number, range 1 trillion
rand_int = random.randint(0, 1e12)
true_root = rand_int ** 0.5
print(f"Number: {rand_int}, its root: {true_root}\n")

guess = rand_int // 1e6 # divide by 1 million
counter = 0 # counts how many guesses made till now.

print("Start approximation")
while True:
    counter += 1

    # improve on the guess
    prev_guess, guess = guess, (rand_int / guess + guess) / 2
    if prev_guess == guess:
        print(f"Found true root after {counter} guesses.")
        break
    print(guess)
