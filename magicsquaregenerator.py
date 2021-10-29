"""
we want to create a magic square of dimensions N x N
here n is provided by the user and the magic square contains no from 1- N*N
we know that the common sum of the rows and cols or diagonals is mean of summation (1- N*N) divided by n
or it is N(N^2+1)/2

now as the magic square has continous numbers we can use this well odering property of natural numbers to our advantage
rules for creating a magic square:
the first no is stored at (n/2,n-1)
and the next element at(i-1,j+1)from rule 1
1.the pos of the next number in the matrix is equal to the row-1 and col+1(where  row and col are location of previous item or no)
if row-1 beomes -1 then it is placed in n-1 and if col+1 becomes greater than or equal to n then it will be 0
2.if the position is filled then new col=col-2 and new row=row+1
3.if the new col=n and new row=-1 then new row, new col =(0,n-2)
"""

def createmagicsquare(n):
    magicsquare=[[0 for x in range(n)]for y in range(n)]
    #location of 1st element is fixed
    i=int(n/2)
    j=n-1
    num=1
    while num<=n*n:
        #checking rule 3
        if i==-1 and j==n:
            i,j=0,n-2
        #to check if the pos are not part of the matrix
        elif j==n:
            #if column is more than the actual no of columns
            j=0
        elif i==-1:
            #if row is less than the actual no of rows i.e the row s location is -1 which is not part of the matrix
            i=n-1
        #checking rule 2
        if magicsquare[i][j]:
            j=j-2
            i=i+1
            continue
        else:
            magicsquare[i][j]=num
            num+=1
        #by rule 1 we determine the location of the next element
        i-=1
        j+=1
    print("common sum = %d"%int(n*(n^2+1)/2))
    for i in magicsquare:
        for j in i:
            print(j,end="\t")
        print()

n=int(input("Enter the size for the magic square: "))
print("The Magic square of size %dx%d is"%(n,n))
createmagicsquare(n)

