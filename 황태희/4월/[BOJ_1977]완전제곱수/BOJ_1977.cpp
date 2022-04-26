#include <stdio.h>
#include<math.h>

int main()
{
    int A, B, a1 = 0, a2;
    scanf("%d", &A);
    scanf("%d", &B);
    if (int(sqrt(B)) == sqrt(A)){
        a1 = A;
        a2 = A;
    }
    else{
        for (int i = int(sqrt(B)); i > int(sqrt(A-1)); i--)
        {
            a1 += i*i;
            a2 = i*i;
        }
    }
    
    if (a1 == 0)
        printf("-1\n");
    else
        printf("%d\n%d", a1, a2);
}
