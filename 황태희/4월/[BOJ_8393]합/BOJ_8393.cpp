#include <stdio.h>


int main()
{
    int n, total = 0;
    scanf("%d", &n);
    for (int i=1; i <= n; i++)
    {
        total += i;
    }
    printf("%d", total);
}
