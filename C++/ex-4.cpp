#include <iostream>
using namespace std;

int main()
{

    float n1, n2;
    cout << "ENTER TWO NUMBERS" << endl;
    cin >> n1 >> n2;

    char op;
    cout << "INPUT AN OPERATOR";
    cin >> op;
    switch (op)
    {
    case '+':
        cout << n1 + n2 << endl;
        break;
    case '-':
        cout << n1 - n2 << endl;
        break;
    case '*':
        cout << n1 * n2 << endl;
        break;
    case '/':
        cout << n1 / n2 << endl;
        break;
    default:
        cout << "INVALID OPERATOR" << endl;
        break;
    }
    return 0;
}