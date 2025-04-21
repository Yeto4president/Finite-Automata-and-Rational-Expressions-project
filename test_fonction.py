from automate import *
def test(num):
    chemin_fichier = f'dossier_automate/BN6-{num}.txt'
    AF = Automate()
    AF.getValue(chemin_fichier)
    with open(f"dossier_trace/BN6-{num}_trace.txt", "w",encoding='utf-8') as file:
        file.write(f"Automate n°{num}\n")
        AF.affiche_test(file)

        # ----------------------------------------------Standardisation --------------------------------------------------------------

        if not AF.est_standard():
            file.write("Automate non standardisé, voulez-vous le standardiser ? Oui ou Non  Oui \n")
            AF.standardiser()
            file.write("Standardisation...\n")
            AF.affiche_test(file)
        else:
            file.write("Automate déjà standardisé\n")
            AF.affiche_test(file)

        # ---------------------------------------Déterminisation et/ou complétion-------------------------------------------------------

        if AF.est_deterministe():
            file.write("Automate déterministe ")
            if AF.est_complet():
                file.write("et complet\n")
                file.write("Affichage de l'automate\n")
                AF.affiche_test(file)
            else:
                file.write("mais non complet\n")
                file.write("Complétion...\n")
                AF.completer()
                AF.affiche_test(file)
        else:
            file.write("Automate ni déterministe ni complet\n")
            file.write("Déterminisation et complétion...\n")
            AF.determination_completion()
            AF.affiche_test(file)

        # -------------------------------------------Complémentaire--------------------------------------------------------------------------

        file.write("Automate complémentaire...\n")
        AF.langage_complementaire()
        AF.affiche_test(file)

        # -------------------------------------------Reconnaissance mot --------------------------------------------------------------------------

        mot = creer_chaine_alphabet(len(AF.alphabets))
        if AF.mot_reconnu(mot) == True :
            file.write(f"Le mot {mot} est reconnu ")
        else :
            file.write(f"Le mot {mot} n'est pas reconnu")



def creer_chaine_alphabet(longueur):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    chaine = (alphabet * (longueur // len(alphabet) + 1))[:longueur]
    return chaine

for i in range (1,45):
    test(i)