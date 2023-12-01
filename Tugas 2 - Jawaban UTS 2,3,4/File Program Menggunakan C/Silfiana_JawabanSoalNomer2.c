#include<stdio.h>

void main(){
    int p[1000];int k[1000];
    int wnew[1000];
    int kk = 0;
    p[1] = 2; p[2] = 4;p[3] = 3;p[4] = 1;p[5] = 3;p[6] = 6;
    p[7] = 4;p[8] = 3;p[9] = 1;p[10] = 0;p[11] = 3;p[12] = 2;
    for (int i = 1; i <=12; i++)
    {
        kk = kk + p[i];
        k[i] = kk;
    }
    for (int i = 1; i <=12; i++)
    {
        wnew[i] = (k[i]*12)/32;
    }
    printf("w | Cw | w-baru\n");

    for (int i = 1; i <=12; i++)
    {
        printf("%d | %d | %d\n", p[i], k[i], wnew[i]);
    }

}
