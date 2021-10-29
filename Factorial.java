importjava.util.*;
public classProgram2
{
public static voidmain(String[] args)
{
Scanner scn=newScanner(System.in);
intfact =1;
System.out.print("Enter a number: ");
intn=scn.nextInt();
for(inti =1; i <=n; i++)
{
fact *= i;
}
System.out.println("Factorial of "+n+" is "+ fact);
}
}
