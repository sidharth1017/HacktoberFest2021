#After space in star(*)
num=int(input("enter no: "))
for a in range(1,num+1):
     print(" "*(num-a)+"* "*a)
for a in range(num-1,0,-1):
    print(" "*(num-a)+"* "*a)