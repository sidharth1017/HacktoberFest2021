// printing of all prime numbers between 2 given numbers.


#include<iostream>
#include<math.h>
using namespace std;

bool isprime(int num){                           // function is made
    for(int i =2;i<=sqrt(num);i++){
        if (num%i==0)
        {
            return false;
        }
        
    }
    return true;
}
int main(){
    int a,b;
    cin>>a>>b;

    for(int i = a; i<=b;i++){
        if (isprime(i))          //we are calling fuction
        {
           cout<<i<<endl;
        }
        


    }
    return 0;
}
