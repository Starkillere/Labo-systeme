#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct Niveau {
    int longueurNombreGauche;
    int longueurNombreDroit;
};

void afficherInterface(int a, int b, int res, int niveau) {
    system("clear"); // Efface l'écran (à remplacer par "cls" sous Windows)

    printf("========== Niveau %d ==========\n", niveau);
    printf("Calcul : %d x %d = %d\n", a, b, res);
    printf("1 - Augmenter la longueur du nombre de gauche\n");
    printf("2 - Diminuer la longueur du nombre de gauche\n");
    printf("3 - Augmenter la longueur du nombre de droite\n");
    printf("4 - Diminuer la longueur du nombre de droite\n");
    printf("0 - Quitter\n");
}

int genererNombre(int longueur) {
    int min = 1;
    int max = 1;
    for (int i = 0; i < longueur; i++) {
        min *= 10;
        max *= 10;
    }
    max = max * 10 - 1;
    return (rand() % (max - min + 1)) + min;
}

int effectuerCalcul(int nombreGauche, int nombreDroit) {
    return nombreGauche * nombreDroit;
}

int main() {
    srand(time(NULL));


    FILE *fichier = fopen("niveau.txt", "r");
    struct Niveau niveauUtilisateur = {2, 2}; // Niveau par défaut
    if (fichier != NULL) {
        fscanf(fichier, "%d %d", &niveauUtilisateur.longueurNombreGauche, &niveauUtilisateur.longueurNombreDroit);
        fclose(fichier);
    }

    int continuer = 1;
    while (continuer) {
        int nombreGauche = genererNombre(niveauUtilisateur.longueurNombreGauche);
        int nombreDroit = genererNombre(niveauUtilisateur.longueurNombreDroit);
        int resultatAttendu = effectuerCalcul(nombreGauche, nombreDroit);

        int reponse;
        int niveau = niveauUtilisateur.longueurNombreDroit;
        do {
            afficherInterface(nombreGauche, nombreDroit, resultatAttendu,  niveau);
            scanf("%d", &reponse);
            switch (reponse) {
                case 1:
                    if (niveauUtilisateur.longueurNombreGauche < niveauUtilisateur.longueurNombreDroit)
                        niveauUtilisateur.longueurNombreGauche++;
                    break;
                case 2:
                    if (niveauUtilisateur.longueurNombreGauche > 1)
                        niveauUtilisateur.longueurNombreGauche--;
                    break;
                case 3:
                    niveauUtilisateur.longueurNombreDroit++;
                    break;
                case 4:
                    if (niveauUtilisateur.longueurNombreDroit > 2)
                        niveauUtilisateur.longueurNombreDroit--;
                    break;
                case 0:
                    continuer = 0;
                    break;
                default:
                    break;
            }
        } while (reponse != 0 && reponse != 1 && reponse != 2 && reponse != 3 && reponse != 4);

        // Sauvegarder le niveau de l'utilisateur dans un fichier
        fichier = fopen("niveau.txt", "w");
        if (fichier != NULL) {
            fprintf(fichier, "%d %d", niveauUtilisateur.longueurNombreGauche, niveauUtilisateur.longueurNombreDroit);
            fclose(fichier);
        }
    }

    return 0;
}