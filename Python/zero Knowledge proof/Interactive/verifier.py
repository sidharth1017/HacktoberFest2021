import socket 
import random
from sympy import *
import json
import helper as h
n=60254176704887048568377189579489538851356170421806890050175939028825164407591
g= 3
def extended_euclidean_algorithm(a, b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t
def inverse_of(n, p):
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd
    if gcd != 1:
        # Either n is 0, or p is not a prime number.
        raise ValueError(
            '{} has no multiplicative inverse '
            'modulo {}'.format(n, p))
    else:
        return x % p
s = socket.socket()
s.connect(('localhost',9999))
s.sendall("Connected with gateway".encode('utf-8'))
t = int(s.recv(1024).decode('utf-8'))
c = h.generate_prime_number()
s.sendall(str(c).encode('utf-8'))
value = s.recv(1024).decode('utf-8')
value=json.loads(value)

r = value.get("r")
y = value.get("y")
v = h.generate_prime_number()
print("r : " + str(r))
if (r<0):
    	Result = ( inverse_of(pow(g,-r,n),n) * pow(y,c,n))  % n
else:
	Result = (pow(g,r,n-1) * pow(y,c,n-1))  % n
print("result : " + str(Result))
if (t==Result):
    	print('x knows the password')
else:
	print('not proven that x is known')
s.sendall("You are verified".encode('utf-8'))
