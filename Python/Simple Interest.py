# Python program to calculate Simple interest:

P = int(input('Enter the principal amount: '))
R = int(input('Enter the rate(number from 0-100): '))
T = int(input('Enter the time in years: '))

# Formula for simple interest: P*R*T

print("Interest: ",P*(R/100)*T)
print("Final Amount: ",P+(P*(R/100)*T))
