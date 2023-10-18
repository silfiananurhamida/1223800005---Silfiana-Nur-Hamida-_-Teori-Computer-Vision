#include<stdio.h>

void main(){
    int X[100][100];
    int V_awal, V_akhir, Qawal, Qakhir;
    int x, y;int Yx, Yy, Ytotal;

    //Matriks
    X[1][1] = 1; X[1][2] = 0;
    X[2][1] = 1; X[2][2] = 1;
    X[3][1] = 1; X[3][2] = 1;
    X[4][1] = 1; X[4][2] = 0;

    X[1][3] = 0; X[1][4] = 0;
    X[2][3] = 1; X[2][4] = 0;
    X[3][3] = 1; X[3][4] = 0;
    X[4][3] = 0; X[4][4] = 0;
    for(int s = 1; s<=10; s++)
    {
        X[10][s] = 0;
        X[s][10] = 0;
    }

    printf("Hasil perhitungan konvolusi dengan metode sobel pada:\n");
    printf("Sebutkan Baris Matriks: ");
    scanf("%d", &x);
    printf("Sebutkan Kolom Matriks : ");
    scanf("%d", &y);

    V_awal = x-1;
    V_akhir = x+1;
    Qawal = y-1;
    Qakhir = y+1;

    if(V_awal<1) V_awal = 10;
    if(V_akhir>4) V_akhir = 10;
    if(Qawal<1) Qawal = 10;
    if(Qakhir>4)Qakhir = 10;

    //implementasi rumus
    Yx = -X[V_awal][Qawal]-2*X[V_awal][y]-X[V_awal][Qakhir]+X[V_akhir][Qawal]+2*X[V_akhir][y]+X[V_akhir][Qakhir];
    Yy = -X[V_awal][Qawal]+X[V_awal][Qakhir]-2*X[x][Qawal]+2*X[x][Qakhir]-X[V_akhir][Qawal]+X[V_akhir][Qakhir];
    Ytotal = Yx+Yy;

    printf("\nNilai dari Y[%d][%d] adalah %d\n\n", x,y,Ytotal);


}
