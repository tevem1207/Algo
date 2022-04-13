#include <stdio.h>

int main()
{
    int h[3], m[3], s[3];
    for (int i=0; i<2; i++)
    {
        scanf("%d:%d:%d\n", &h[i], &m[i], &s[i]);
    }
    
    h[2] = h[1]-h[0];
    m[2] = m[1]-m[0];
    s[2] = s[1]-s[0];
    
    if (s[2] < 0)
    {
        m[2]--;
        s[2] += 60;
    }
    if (m[2] < 0)
    {
        h[2]--;
        m[2] += 60;
    }
    if (h[2] < 0) h[2] += 24;
    
    
    printf("%02d:%02d:%02d\n", h[2], m[2], s[2]);
}
