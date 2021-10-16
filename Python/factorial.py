def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact = fact * num
    return(fact)