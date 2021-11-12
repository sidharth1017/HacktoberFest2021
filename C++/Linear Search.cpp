#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        cout << "enter element " << i + 1 << " :";
        cin >> arr[i];
    }
    int num;
    cout << "Enter the number u want to search: ";
    cin >> num;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == num)
        {
            cout << "The number is present at position " << i + 1;
            break;
        }
        if (i == n - 1)
        {
            cout << "The number is not present";
        }
    }
}
