// Question-- Find the first occurence and last occurence of sorted array.
// OR Find the lower bound and upper bound of sorted array.

#include<iostream>
using namespace std;

int firstocc(int a[],int n,int key){
    int s=0;
    int e= n-1;
    int ans= -1;

    while (s<=e)
    {
       int mid= (s+e)/2;
       
       if (a[mid]==key)
       {
           ans=mid;
           e=mid-1;
       }
       else if (a[mid]>key){
           e=mid-1;
       }
       else
       {
           s=mid+1;
       }
       
       
    }
    return ans;
    
     
}

int main(){
    int a[]={1,2,2,2,2,4,4};
    int n=sizeof(a)/sizeof(int);
    int key=2;

    int ans=firstocc(a,n,key);
    cout<<"First occurence of 2  is  "<<ans<<endl;
    return 0;
}