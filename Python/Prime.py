import math
def checkprime(n):
    for i in range(2,int(math.sqrt(n))):
        if(n%i==0):
            return ("Not prime")
    return "prime"

n=int(input("Interger to check whether it's prime or not:"))
print(checkprime(n))
