#include<iostream>
using namespace std;
int lcsD(string s1,string s2 )
{
    int**arr = new int*[s1.size()+1];
    for(int i = 0 ; i <= s1.size(); i++)
    {
        arr[i] = new int[s2.size()+1];
    }
    // filling 1st row
    for(int i = 0 ;  i < s1.size() ; i++)
    {
        arr[0][i] = 0;
    }
    // filling 1st column
    for(int i = 1 ; i <= s2.size() ; i++)
    {
        arr[i][0] = 0;
    }
    //filling rest of the entries
    for(int i = 1 ; i <= s1.size() ; i++)
    {
        for(int j = 1 ; j <= s2.size() ; j++)
        {
            if(s1[i-1] == s2[j-1])
            {
                arr[i][j] = 1+ arr[i-1][j-1];
            }
            else
            {
                arr[i][j] = max(arr[i-1][j] , arr[i][j-1]);
            }
        }
    }return arr[s1.size()][s2.size()];




}
int lcs_mem(string s1 , string s2 , int n , int m,int**output)
{
    if(m==0 || n==0)
    {
        return 0;
    }
    if(output[n][m]!=-1)
    {
        return output[n][m];
    }
    if(s1[0] == s2[0])
    {
        output[n][m] =  1+lcs_mem(s1.substr(1),s2.substr(1), n-1 , m-1,output);
        return output[n][m];
    }
    int smallAns = max(lcs_mem(s1.substr(1), s2 , n-1 , m,output), lcs_mem(s1,s2.substr(1),n,m-1,output));
    output[n][m] = smallAns;
    return output[n][m];

}
int lcs(string s1 , string s2 , int n, int m)
{
    //base case
    if(m==0 || n==0)
    {
        return 0;
    }
    if(s1[0] == s2[0])
    {
        return 1+lcs(s1.substr(1),s2.substr(1), n-1 , m-1);
    }
    return max(lcs(s1.substr(1), s2 , n-1 , m), lcs(s1,s2.substr(1),n,m-1));
}

int main()
{
    string s1,s2;
    cin >> s1;
    cin >> s2;
	int n = s1.size(), m = s2.size();
    int**output = new int*[n+1];
    for(int i = 0 ; i <= n ; i++)
    {
        output[i] = new int[m+1];
        for(int j = 0 ; j <= m ; j++)
        {
            output[i][j] = -1;
        }
    }
    // cout<< lcsD(s1,s2)<<endl;
    // cout<<lcs_mem(s1,s2,n,m,output)<<endl;
    cout<< lcs(s1,s2,n,m)<<endl;
    return 0;
}

// This code is contributed by Adhyayan Rajpoot