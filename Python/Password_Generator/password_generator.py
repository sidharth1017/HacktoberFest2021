import random #Importing random library
import numpy as np #importing numpy as np
s1={0,1,2,3,4,5,6,7,8,9} #Initialising a set for digits
s2={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'} #Initialising a set for small letters
s3={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'} #Initialising a set for capital letters
s4={'!','@','#','$','%','^','&','*'} #Initialising a set for symbols
#Concatenating the sets into s
s = s1.union(s2)
s = s.union(s3)
s = s.union(s4)
#Converting into list
s1=list(s1)
s2=list(s2)
s3=list(s3)
s4=list(s4)
s=list(s)
pass_w=list()
#Generating random password into pass_w
pass_w.append(random.choice(s1))
pass_w.append(random.choice(s2))
pass_w.append(random.choice(s3))
pass_w.append(random.choice(s4))
n=int(input())
#Checking whether the length of the password is long enough
if(n<4):
    print("Length is too short!")
else:
    for i in range(n-4):
        pass_w.append(random.choice(s))
#Assigning ans as numpy
ans=np.array(pass_w)
np.random.shuffle(ans)
#Displaying the password
for i in ans:
    print(i,end="")
print()