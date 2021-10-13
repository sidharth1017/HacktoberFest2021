// This is the example of wave sort which is asked in google interview.

#include<iostream>
using namespace std;

int main(){
    int a[]={1,3,4,2,7,8};
    int n=sizeof(a)/sizeof(int);

    // go to every 2nd element and try to create peak.0
    for(int i=0; i<n; i+=2)
    {
        // check for left element
        if (i>0&&a[i-1]>a[i])
        {
           swap(a[i],a[i-1]);
        }
        
        // check for right element
        if (i<=n-2 &&a[i+1]>a[i])
        {
           swap(a[i],a[i+1]);
        }
        
    }
    // print the array
    for (int i = 0; i < n; i++)
    {
        cout<<a[i]<<endl;
    }
    
    return 0;
}