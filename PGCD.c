#include <stdio.h>
#include <stdlib.h>

int pgcd(int a, int b);
void algorithmeEucluide(int a, int b);

int main(int argc, char** argv)
{
    int a = 0;
    int b = 0;
    int mode = 0;

    printf("\n: ");
    scanf("%d", &a);
    printf("\n: ");
    scanf("%d", &b);
    printf("\nmode: ");
    scanf("%d", &mode);
    if (mode == 1)
    {
        printf(pgcd(a, b));
    }
    
    else
    {
        algorithmeEucluide(a, b);
    }

}

int pgcd(int a, int b)
{
    int res = 0;
    int reste = 0;
    int coeff = 0;
    int postreste = 0;

    if (a >= b) {

        res = a;
        coeff = b;
    }

    else
    {
        res = b;
        coeff = a;
    }

    do
    {
       coeff = res/coeff;
       postreste = reste;
       reste = res%coeff;
       res = coeff;

    } while (reste != 0);
    
    return(postreste);
}

void algorithmeEucluide(int a, int b)
{
    int res = 0;
    int reste = 0;
    int coeff = 0;
    int postreste = 0;

    if (a >= b) {

        res = a;
        coeff = b;
    }

    else
    {
        res = b;
        coeff = a;
    }

    do
    {
       printf("%d = %d*%d + %d\n", res, coeff, res/coeff, res%coeff);
       coeff = res/coeff;
       postreste = reste;
       reste = res%coeff;
       res = coeff;

    } while (reste != 0);
    
    printf("PGCD(%d, %d) = %d\n", a, b, postreste);
}