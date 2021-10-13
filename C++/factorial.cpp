// // factorial of a given number

#include<iostream>
using namespace std;


int fact(int n){
    int factorial=1;
    for ( int i = 2; i <=n; i++)
    {
    factorial = factorial*i;
    }
    return factorial;
}

int main(){
    int n;
    cin>>n;
     fact(n);
     cout<<fact(n);
    return 0;
}