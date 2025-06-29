#include <iostream>
using namespace std;

int res[10];
int col[10];
int di1[20];
int di2[20];

void print(int a[10], int n);
void nQueens(int n, int i);

void print(int a[10], int n)
{
    cout << "[";
    for (int i = 1; i < n; i++)
    {
        cout << a[i] << ", ";
    }
    cout << a[n] << "]" << endl;
}

void nQueens(int n, int i)
{
    for (int j = 1; j <= n; j++)
    {
        if (col[j] == 1 && di1[i - j + n] == 1 && di2[i + j - 1] == 1)
        {
            res[i] = j;
            col[j] = di1[i - j + n] = di2[i + j - 1] = 0;
            if (i == n)
            {
                print(res, n);
            }
            else
            {
                nQueens(n, i + 1);
            }
            col[j] = di1[i - j + n] = di2[i + j - 1] = 1;
        }
    }
}

int main()
{
    int n;
    cin >> n;
    while (n < 1 || n > 10)
    {
        cin >> n;
    }
    for (int i = 1; i <= n; i++)
    {
        col[i] = 1;
    }
    for (int i = 1; i <= 2 * n; i++)
    {
        di1[i] = di2[i] = 1;
    }
    nQueens(n, 1);

    return 0;
}
