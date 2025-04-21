from automate import *

if __name__ == "__main__":
    Terminer = False
    Defined = False
    AF = Automate()

    while Terminer == False :
        print("\n")
        print("Que voulez vous faire ?")
        print("1 - Charger un automate")
        print("2 - Standardiser l'automate")
        print("3 - Déterminiser et/ou compléter l'automate")
        print("4 - Afficher l'automate complémentaire")
        print("5 - Tester la reconnaissance de mot sur l'automate ")
        print("6 - Quitter le programme ")
        choix = int(input())
        while  choix < 1 or choix > 6 :
            print("Choix incorrect, réessayer")
            choix = int(input())

        # ----------------------------------------------Chargement des automates --------------------------------------------------------------
        if choix == 1 :
            num = int(input("Choisir un automate ( de 1 à 44 ) : "))
            chemin_fichier = f'dossier_automate/BN6-{num}.txt'
            AF.getValue(chemin_fichier)
            print(f"Automate n{num}")
            AF.afficher_table_transitions()
            Defined = True

        # ----------------------------------------------Standardisation --------------------------------------------------------------
        if choix == 2 :
            if Defined == False :
                print("Aucun automate charger")

            else :
                if AF.est_standard() == False :
                    if input("Automate non standardiser, voulez-vous le standardiser ? Oui ou Non ") == "Oui" :
                        AF.standardiser()
                        print("Standardisation...")
                        AF.afficher_table_transitions()
                else :
                    print("Automate déjà standardiser")
                    AF.afficher_table_transitions()

        # ---------------------------------------Déterminisation et/ou complétion-------------------------------------------------------

        if choix == 3 :
            if Defined == False :
                print("Aucun automate charger")

            else :
                if AF.est_deterministe() :
                    print("Automate déterministe", end =" ")
                    if AF.est_complet() :
                        print("et complet")
                        print("Affichage de l'automate")
                        AF.afficher_table_transitions()
                    else :
                        print("mais non complet")
                        print("Complétion...")
                        AF.completer()
                        AF.afficher_table_transitions()
                else :
                    print("Déterminisation et complétion...")
                    AF.determination_completion()
                    AF.afficher_table_transitions()

        # -------------------------------------------Complémentaire-------------------------------------------------------------
        if choix == 4 :
            if Defined == False :
                print("Aucun automate charger")
            else :
                print("Automate complémentaire...")
                AF.langage_complementaire()
                AF.afficher_table_transitions()

        # -------------------------------------Reconnaissance de mot --------------------------------------------------------------------
        if choix == 5 :
            if Defined == False :
                print("Aucun automate charger")
            else :
                mot = str(input("Choisir le mot à reconnaitre "))
                if AF.mot_reconnu(mot) == True :
                    print(f"le mot {mot} est bien reconnue")
                else :
                    print("Mot non reconnu")

        # ------------------------------------- Fin --------------------------------------------------------------------
        if choix == 6 :
            Terminer = True