def primeCheck(n):
    # 0, 1, even numbers greater than 2 are NOT PRIME
    if n==1 or n==0 or (n % 2 == 0 and n > 2):
        return "Not prime"
    else:
        # Not prime if divisable by another number less
        # or equal to the square root of itself.
        # n**(1/2) returns square root of n
        for i in range(3, int(n**(1/2))+1, 2):
            if n%i == 0:
                return "Not prime"
        return "Prime"