#include<iostream>
using namespace std;
int editDistanceDP(string s1 , string s2)
{
    int m = s1.size();
    int n = s2.size();
    int**output = new int*[m+1];
    for(int i = 0 ; i <=m ; i++)
    {
        output[i]=  new int[n+1];
    }

    for(int i = 0; i <= n ; i++)
    {
        output[0][i] = i;
    }
    for(int i = 0 ; i <= m ; i++)
    {
        output[i][0] = i;
    }

    for(int i = 1 ; i <= m ; i++)
    {
        for(int j = 1 ; j <= n ; j++)
        {
            if(s1[i-1] == s2[j-1])
            {
                output[i][j] = output[i-1][j-1];
            }
            else{
                output[i][j] = 1+min(output[i-1][j],min(output[i][j-1],output[i-1][j-1]));
            }
        }
    }
    return output[m][n];
}
int editDistance(string s1,string s2 , int**output)
{
    int m = s1.size();
    int n = s2.size();
    if(m==0) return n;
    if(n==0) return m;
    if(output[m][n]!=-1)
    {
        return output[m][n];
    }
    int smallAns;
    if(s1[0]==s2[0])
    {
        smallAns = editDistance(s1.substr(1),s2.substr(1),output);
    }
    else
        smallAns = 1+min(editDistance(s1.substr(1),s2,output),min(editDistance(s1,s2.substr(1),output),editDistance(s1.substr(1),s2.substr(1),output)));
    output[m][n] = smallAns;
    return smallAns;
}
int editDistance(string s1,string s2)
{
    int m = s1.size();
    int n = s2.size();
    if(m==0)
    {
        return n;
    }
    if(n==0)
    {
        return m;
    }

    if(s1[0]==s2[0])
    {
        return editDistance(s1.substr(1),s2.substr(1));
    }
    else
    {
        return 1+min(editDistance(s1.substr(1),s2),min(editDistance(s1,s2.substr(1)),editDistance(s1.substr(1),s2.substr(1))));
    }
}
int main()
{
    string s1,s2;
    cin >> s1 >> s2;
    int m = s1.size();
    int n = s2.size();
    int**output = new int*[m+1];
    for(int i = 0 ; i <= m ; i++)
    {
        output[i] = new int[n+1];
        for(int j = 0; j <= n ; j++)
        {
            output[i][j] = -1;
        }
    }
    cout << editDistanceDP(s1,s2)<<endl;
    cout<< editDistance(s1,s2,output) << endl;
    cout<< editDistance(s1,s2) << endl;
}

// This code is contributed by Adhyayan Rajpoot