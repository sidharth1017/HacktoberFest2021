#Program to calculate multiplication table of any number for n number of times.
print("Multiplication table calculator.")
x=int(input("Enter a number for multiplication table: "))
y=int(input("Enter a value for the number of multiplication tables: "))
for i in range(1,y+1):
  print(i,"x",x ,"= ",x*i)
