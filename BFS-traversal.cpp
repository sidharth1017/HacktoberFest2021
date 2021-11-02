//
//  main.cpp
//  BFS Traversal
//
//  Created by Adhyayan Rajpoot on 26/10/21.
//

#include <iostream>
using namespace std;
#include<queue>

void printBFS(int **edges , int n ,int sv ,bool*visited)
{
    queue<int> pendingVertices;
    pendingVertices.push(sv);
    visited[sv] = true;
    while(!pendingVertices.empty())
    {
        int currentVertex = pendingVertices.front();
        pendingVertices.pop();
        cout << currentVertex << " ";
        for(int i = 0 ; i < n ; i++)
        {
            if(currentVertex == i)
            {
                continue;
            }
            if(edges[currentVertex][i] == 1 && !visited[i])   //  && !visited[i] because if we travel 01 in first case then we have to take care of 10 as well
            {
                pendingVertices.push(i);
                visited[i] = true;
            }
        }
    }
}

int main() {
    // insert code here...
    int n , e;  //  n -> vertex ; e -> edge
    cin >> n >> e;
    //
    int **edges = new int*[n];
    //LOOPING TO INITIALISE 2D ARRAY TO 0   -> IMAGINE A SPARCE MATRIX !
    for(int i = 0 ; i < n ; i++)
    {
        edges[i] = new int [n];
        for(int j= 0 ; j < n ;j++)
        {
            edges[i][j] = 0;
        }
    }//LOOPING TO SHOW THAT THE ELEMENT IS PRESENT  BY ASSIGNING AT THE POSITION = 1
    for(int i = 0 ; i < e ; i++) //here we have taken e instead of n because we are taking input in pair like a H2O molecule    1, 2 -> 12
    {
        int f,s;
        cin >> f >> s;
        edges[f][s] = 1;
        edges[f][s] = 1;
    }
    //CREATING  A 1D ARRAY SO THAT WE CAN CHECK WHETHER WE HAVE TRAVELLED THROUGH THAT VERTEX OR NOT
    bool*visited = new bool [n];
    //INITIALISING ARRAY WITH FALSE INDICATING WE HAVE NOT TRAVELLED ANY OF THEM TILL NOW
    for(int i = 0 ; i < n ; i++)
    {
        visited[i] = false;
    }
    for(int sv = 0 ; sv < n ; sv++)
    {
        if(!visited[sv])
        {
            printBFS(edges , n, sv , visited);
        }
    }
    for(int i = 0 ; i < n ; i++)
    {
        delete [] edges[i];
    }
    delete [] edges;
    delete [] visited;
    return 0;
}
// This code is contributed by Adhyayan Rajpoot
