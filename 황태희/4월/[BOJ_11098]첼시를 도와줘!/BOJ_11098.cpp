#include <stdio.h>
#include <string.h>


int main()
{
    int n, p, C;
    char name[20];
    scanf("%d", &n);
    for (int i = 0; i<n; i++)
    {
        int max_C=0;
        char answer[20];
        scanf("%d", &p);
        for (int i = 0; i<p; i++)
        {
            scanf("%d %s", &C, name);
            if (max_C<C){
                strcpy(answer, name);
                max_C = C;
                }
        }
        printf("%s\n", answer);
    }
}
