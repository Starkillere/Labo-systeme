#include <stdio.h>
#include <stdlib.h>

int valeurAbsolue(int n);
int nombreDeDiviseur(int n);
void calculeDiviseur(int n, int* tableDiviseur);
void tri_selection(int* table, int lenght);
void affichage(int* table, int lenght);

int main (int argc, char** argv)
{
    int nombre = 0;
    int absolutNombre = 0;
    int* table = NULL;
    int nombreDiviseurN = 0;
    int length = 0;

    printf("Nombre dont vous souhaiter conaitre les diviseur: ");
    scanf("%d", &nombre);

    if (nombre == 0)
    {
        printf("\nL'emsemble des diviseur de 0 est Z*");
        return(0);
    }
    
    absolutNombre = valeurAbsolue(nombre);
    nombreDiviseurN = nombreDeDiviseur(absolutNombre);
    length = nombreDiviseurN-1;
    table = malloc(length*sizeof(int));

    if (table == NULL)
    {
        exit(1);
    }

    calculeDiviseur(absolutNombre, table);
    tri_selection(table, length);
    affichage(table, length);

    free(table);
    return (0);

}

int valeurAbsolue(int n)
{
    if (n < 0)
    {
        return (-n);
    }
    
    return (n);
}

int nombreDeDiviseur(int n)
{
    int diviseur_min = 1;
    int diviseur_max = n;
    int i = 1;
    while (diviseur_max >= diviseur_min)
    {
        if (n%diviseur_min == 0)
        {
            i = i + 2;
            if (diviseur_min != diviseur_max)
            {
                i = i + 2;
            }
            
        }
        diviseur_min++;
        diviseur_max = n/diviseur_min;
    }
    return (i);
}

void calculeDiviseur(int n, int* tableDiviseur)
{
    int diviseur_min = 1;
    int diviseur_max = n;
    int i = 0;
    while (diviseur_max >= diviseur_min)
    {
        if (n%diviseur_min == 0)
        {
            tableDiviseur[i] = diviseur_min;
            tableDiviseur[i+1] = -diviseur_min;
            if (diviseur_min != diviseur_max)
            {
                tableDiviseur[i+2] = diviseur_max;
                tableDiviseur[i+3] = -diviseur_max;
            }
            i = i + 4;
        }
        diviseur_min++;
        diviseur_max = n/diviseur_min;
    }
    
}

void tri_selection(int* table, int lenght)
{
    int var = 0;
    for (int i = 0; i < lenght; i++)
    {
        for (int j = 0; j < lenght; j++)
        {
            if (table[i] < table[j])
            {
                var = table[i];
                table[i] = table[j];
                table[j] = var;
            }
        }
    }
}

void affichage(int* table, int lenght)
{
    printf("{ ");
    for (int i = 0; i < lenght; i++)
    {
        if (i != lenght-1)
        {
            printf("%d ; ",table[i]);
        }
        else
        {
            printf("%d",table[i]);
        }
    }
    printf(" }");
}