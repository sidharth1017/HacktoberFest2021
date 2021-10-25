#Bhaskara's formula

while True:
    try:
        a, b, c = map(int, input("Please insert the values for A, B and C as Ax^2 + Bx + C = 0.\n").split())
        if a != 0:
            delta = b**2 - 4 * a * c
            if delta>0:
                x1, x2 = (delta**(0.5) - b)/(2*a), (-(delta**(0.5)) - b)/(2*a)
                print("The solutions for the equation you entered are: {}, {}\n".format(x1, x2))
            elif delta==0:
                x = (-b)/(2*a)
                print("The solution for the solution you entered is: {}\n".format(x))
            else:
                print("The equation you entered has no solutions in the set of real numbers.\n")
        elif (a==0) and (b!=0):
            x = -c/b
            print("The equation you entered doesn't actually need to use Bhaskara's formula. The solution is {}\n".format(x))
        else:
            print("The values you entered don't form an equation.\n")
    except ValueError:
        break