import java.util.*;

class Fibonacci

{

public static void main(String args[])

{

int n;

System.out.println("Enter the number of terms:");

Scanner input=new Scanner(System.in);

n=input.nextInt();

int first=0,second=1;

System.out.println("The series is==>");

System.out.println(first);

System.out.println(second);

for(int i=0;i<(n-2);i++)

{

int temp=first+second;

first=second;

second=temp;

System .out.println(temp);

} }
