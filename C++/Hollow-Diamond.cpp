#include <iostream>
using namespace std;
int main() 
{
    int N;
    N = 10;
    int hn=(N+1)/2;
    int equi,equj;
    for(int i=1;i<=N;i++)
    {
        for(int j=1;j<=N;j++)
        {
            if(i<=hn)
            {
                equi=i;
                cout<<" ";
            }
            else
           {
               equi=N-i+1;
               cout<<" ";
           }
           if(j<=hn)
           {    equj=j;
           }
           else
           {
               equj=N-j+1;
           }
         if(equi+equj<=hn+1)
         {
             cout<<"*";
         }
         else
         {
             cout<<" ";
         }
        }
        cout<<endl;
    }
}