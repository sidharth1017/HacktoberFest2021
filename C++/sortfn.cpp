#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int a[]={5,4,3,1,2,6,7};
    int n=sizeof(a)/sizeof(int);

    sort(a,a+n);

    for (int i = 0; i < n; i++)
    {
       cout<<a[i]<<" ";
    }
    
    return 0;
}