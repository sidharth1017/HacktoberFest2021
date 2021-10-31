# import sys
# sys.setrecursionlimit(5000)
# def goodEnough(guess, x):
#     return abs((x - (guess * guess))) <= 0.1

# def newGuess(guess, x):
#     return (guess + guess/x)/2

# def root(guess, x):
#     if goodEnough(guess, x):
#         return guess
#     else:
#         return root(newGuess(guess, x), x)

# def sqrt(x):
#     return root(float(x)/2, float(x)) #x/2 is usually somewhat close to the square root of a number

# def main():
#   y = input("Enter number to calculate Square Root ")
#   print("Square Root is ")
#   result = sqrt(float(y))
#   print(result)
#
#
# Previous code using recursion not on all editors it working
# Take this challenge and solve upper code
# Original topic here https://stackoverflow.com/questions/16005123/how-can-i-make-a-recursive-square-root-in-python

def sqrt(x):
    last_guess= x/2.0
    while True:
        guess= (last_guess + x/last_guess)/2
        if abs(guess - last_guess) < .001: # example threshold
            return guess
        last_guess= guess

def main():
  y = input("Enter number to calculate Square Root ")
  print("Square Root is ")
  result = sqrt(float(y))
  r1 = '%.3f'%(result)
  print (r1)

if __name__ == "__main__":
    main()
