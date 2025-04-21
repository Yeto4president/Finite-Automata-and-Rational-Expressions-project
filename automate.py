class Automate:
    def __init__(self):
        self.alphabets, self.etats, self.initiaux, self.terminaux, self.transitions = None, None, None, None,None
        self.table_transitions = None
        self.nouvel_etat = 'i'

    # Récupération des données

    def getValue(self,chemin):
        self.alphabets, self.etats, self.initiaux, self.terminaux, self.transitions = self.lire_fichier(chemin)
        self.table_transitions = self.construire_table_transitions()

    #Constructeur de copie
    def copie(self):
        NewAutomate = Automate()
        NewAutomate.alphabets = self.alphabets
        NewAutomate.etats = self.etats
        NewAutomate.initiaux = self.initiaux
        NewAutomate.terminaux = self.terminaux
        NewAutomate.transitions = self.transitions
        NewAutomate.table_transitions = self.table_transitions
        return NewAutomate

    #Affichage

    def lire_fichier(self, chemin):
        with open(chemin, 'r',encoding='utf-8') as fichier:

            liste_lignes = fichier.read().splitlines()

            liste_alphabets = self.filtrer_contenu(liste_lignes, 0, 4, ',')
            liste_etats = self.filtrer_contenu(liste_lignes, 1, 4, ',')
            liste_initiaux = self.filtrer_contenu(liste_lignes, 2, 4, ',')
            liste_terminaux = self.filtrer_contenu(liste_lignes, 3, 4, ',')

            liste_transitions = []
            for ligne in liste_lignes[4:]:
                liste_transitions.append(ligne)

            return liste_alphabets, liste_etats, liste_initiaux, liste_terminaux, liste_transitions

    def filtrer_contenu(self, contenu, num_ligne, num_caractere, separateur):
        return contenu[num_ligne][num_caractere:].split(separateur)

    def construire_table_transitions(self):
        table_transitions = [
            [' ' for _ in range(len(self.alphabets))] for _ in range(len(self.etats))]
        for transition in self.transitions:
            temp = transition.split(',')
            ligne = self.etats.index(temp[0])
            col = self.alphabets.index(temp[1])

            if table_transitions[ligne][col] != ' ':
                cellule = table_transitions[ligne][col].split(',')
                if temp[2] not in cellule:
                    table_transitions[ligne][col] += ',' + temp[2]

            else:
                table_transitions[ligne][col] = temp[2]
        return table_transitions

    def afficher_table_transitions(self):
        # Calcul de la largeur maximale pour la colonne des états
        max_etats_width = max(len(etat) for etat in self.etats)

        # Calcul de la largeur maximale pour chaque colonne de l'alphabet
        max_col_widths = [max_etats_width] + [len(alphabet) for alphabet in self.alphabets]
        for i in range(len(self.table_transitions)):
            for j, alphabet in enumerate(self.alphabets):
                if self.table_transitions[i][j] is not None:
                    max_col_widths[j + 1] = max(max_col_widths[j + 1], len(self.table_transitions[i][j]))

        # Affichage de la première ligne : alphabet
        print(' ' * (max_etats_width + 3), end='')  # Espaces pour aligner avec les flèches
        for i, alphabet in enumerate(self.alphabets):
            print(f'| {alphabet:<{max_col_widths[i + 1]}}', end=' ')
        print("|", end="")

        # Affichage du reste de la table (flèches, états et transitions)
        for i in range(len(self.table_transitions)):
            print()
            fleche = self.get_arrow(self.etats[i])
            print(f'{fleche} {self.etats[i]:<{max_etats_width}} | ', end='')
            for j in range(len(self.alphabets)):
                if self.table_transitions[i][j] is None:
                    print(' ' * max_col_widths[j + 1], end=' ')
                else:
                    print(f'{self.table_transitions[i][j]:<{max_col_widths[j + 1]}}', end=' | ')

        # Retour à la ligne
        print("")

    def affiche_test(self, fichier):
        # Calcul de la largeur maximale pour la colonne des états
        max_etats_width = max(len(etat) for etat in self.etats)

        # Calcul de la largeur maximale pour chaque colonne de l'alphabet
        max_col_widths = [max_etats_width] + [len(alphabet) for alphabet in self.alphabets]
        for i in range(len(self.table_transitions)):
            for j, alphabet in enumerate(self.alphabets):
                if self.table_transitions[i][j] is not None:
                    max_col_widths[j + 1] = max(max_col_widths[j + 1], len(self.table_transitions[i][j]))

        # Affichage de la première ligne : alphabet
        fichier.write(' ' * (max_etats_width + 3))  # Espaces pour aligner avec les flèches
        for i, alphabet in enumerate(self.alphabets):
            fichier.write(f'| {alphabet:<{max_col_widths[i + 1]}} ')
        fichier.write("|")

        # Affichage du reste de la table (flèches, états et transitions)
        for i in range(len(self.table_transitions)):
            fichier.write("\n")
            fleche = self.get_arrow(self.etats[i])
            fichier.write(f'{fleche} {self.etats[i]:<{max_etats_width}} | ')
            for j in range(len(self.alphabets)):
                if self.table_transitions[i][j] is None:
                    fichier.write(' ' * max_col_widths[j + 1])
                else:
                    fichier.write(f'{self.table_transitions[i][j]:<{max_col_widths[j + 1]}} | ')

        # Retour à la ligne
        fichier.write("\n")

    def get_arrow(self,etat):
        if etat in self.initiaux and etat in self.terminaux:
            return "↔"
        elif etat in self.initiaux:
            return "→"
        elif etat in self.terminaux:
            return "←"
        else:
            return " "

    # Standardisation

    def est_standard(self):
        # Un seul état initial
        if len(self.initiaux) == 1:
            etat_initial = self.initiaux[0]
            for transition in self.transitions:
                temp = transition.split(',')
                # Aucune transition ne doit arriver sur l'état initial
                if temp[2] == etat_initial:
                    print("Automate non standardiser car tranistion mène à l'état initial",end="")
                    return False
            return True

        else :
            print("Automate non standardiser car nombre d'état initial > 1",end="")
            return False

    def standardiser(self):
        etats_std = self.etats.copy()
        terminaux_std = self.terminaux.copy()
        transitions_std = self.transitions.copy()

        initiaux_reconnait_mot_vide = False
        for etat in self.initiaux:
            if etat in self.terminaux:
                initiaux_reconnait_mot_vide = True
            for transition in self.transitions:
                temp = transition.split(',')
                if temp[0] == etat:
                    transitions_std.append(self.nouvel_etat + ',' + temp[1] + ',' + temp[2])
        initiaux_std = [self.nouvel_etat]
        etats_std.append(self.nouvel_etat)
        if initiaux_reconnait_mot_vide:
            terminaux_std.append(self.nouvel_etat)

        self.etats, self.initiaux, self.terminaux, self.transitions = etats_std, initiaux_std, terminaux_std, transitions_std
        self.table_transitions = self.construire_table_transitions()

        return

    # Determination

    def est_deterministe(self):
        if len(self.initiaux) != 1:
            print("Automate non déterministe car nombre d'état initial > 1", end="")
            return False

        for ligne in range(len(self.table_transitions)):
            for colonne in range(len(self.table_transitions[ligne])):
                etat_actuel = self.table_transitions[ligne][colonne]

                if "," in etat_actuel:
                    print("Automate non déterministe car 2 transitions sortantes (ou plus) étiquettées par la même lettre.")
                    return False

        return True

    def determinisation(self):
        #Cas où il n'y a pas epsilon dans l'alphabet
        if 'ε' not in self.alphabets:
            # Si l'automate a plus d'un état initial, créez un nouvel état initial unique.
            if len(self.initiaux) > 1:
                nouvel_etat_initial = ','.join(sorted(self.initiaux))
                self.initiaux = [nouvel_etat_initial.replace(',', '')]
            else:
                nouvel_etat_initial = self.initiaux[0]
            nouveaux_etats = {nouvel_etat_initial.replace(',', '')}
            nouvelles_transitions = []
            nouveaux_terminaux = set()
            file_traitement = [nouvel_etat_initial]
            # Parcourir l'automate pour créer le DFA.
            while file_traitement: # Tant que chaque état du nouvel état (combinaison de plusieurs états) n'est pas vide
                etat_courant = file_traitement.pop(0) # On dépile le premier élement
                for symbole in self.alphabets:
                    etats_suivants = set()
                    for sous_etat in etat_courant.split(','): # On lit chaque sous-état des états assemblés.
                        for transition in self.transitions: # On lit chaque transitions de l'automate
                            depart, alph, arrivee = transition.split(',')
                            if depart == sous_etat and alph == symbole: #On compare si l'état de départ dé la transition courante correspond au sous-état de l'état actuel et que l'alphabet correspond également
                                etats_suivants.add(arrivee)
                    if etats_suivants:
                        nouvel_etat = ','.join(sorted(etats_suivants))
                        etat_dfa = nouvel_etat.replace(',', '')
                        if etat_dfa not in nouveaux_etats:
                            nouveaux_etats.add(etat_dfa)
                            file_traitement.append(nouvel_etat)
                            if any(etat in self.terminaux for etat in etats_suivants):
                                nouveaux_terminaux.add(etat_dfa)
                        nouvelles_transitions.append(f"{etat_courant.replace(',', '')},{symbole},{etat_dfa}")
            self.etats = list(nouveaux_etats)
            self.transitions = nouvelles_transitions
            self.terminaux = list(nouveaux_terminaux)
        #Cas où epsilon est présent dans l'alphabet
        else:
            fermetures_epsilon = {} # On crée un dict pour stocker chaque état avec comme valeur leur fermeture_epsi
            for etat in self.etats:
                fermetures_epsilon[etat] = self.fermeture_epsilon(etat) # On appelle la fonction permettant de trouver les fermetures epsilons

            # Définissez l'ensemble initial et la file de traitement avec la fermeture de l'état initial
            etat_initial = ','.join(sorted(fermetures_epsilon[self.initiaux[0]]))
            file_traitement = [etat_initial]
            nouveaux_etats = {etat_initial.replace(',', '')}
            nouvelles_transitions = []
            nouveaux_terminaux = set()
            while file_traitement:
                etat_courant = file_traitement.pop(0)
                for symbole in self.alphabets:
                    if symbole != 'ε':  # On ignore les transitions avec epsilons
                        etats_suivants = set()
                        for sous_etat in etat_courant.split(','):
                            for etat_epsilon in fermetures_epsilon[sous_etat]:
                                for transition in self.transitions:
                                    depart, alph, arrivee = transition.split(',')
                                    if depart == etat_epsilon and alph == symbole:
                                        etats_suivants.update(fermetures_epsilon[arrivee])
                        if etats_suivants:
                            nouvel_etat = ','.join(sorted(etats_suivants))
                            etat_dfa = nouvel_etat.replace(',', '')
                            if etat_dfa not in nouveaux_etats:
                                nouveaux_etats.add(etat_dfa)
                                file_traitement.append(nouvel_etat)
                                if any(etat in self.terminaux for etat in etats_suivants):
                                    nouveaux_terminaux.add(etat_dfa)
                            nouvelles_transitions.append(f"{etat_courant.replace(',', '')},{symbole},{etat_dfa}")

            # Mise à jour de l'automate
            self.etats = sorted(list(nouveaux_etats))
            self.transitions = sorted(nouvelles_transitions)
            self.terminaux = sorted(list(nouveaux_terminaux))
            self.initiaux = etat_initial.replace(',','')
            self.alphabets.remove("ε")
        return

    def fermeture_epsilon(self, etat):
        fermeture = [etat]  # On commence avec l'état de base
        i = 0  # Un index pour suivre la position actuelle

        while i < len(fermeture):
            etat_courant = fermeture[i]
            for transition in self.transitions:
                depart, alph, arrivee = transition.split(',')
                if depart == etat_courant and alph == 'ε':
                    if arrivee not in fermeture:  # on ajoute seulement si l'état d'arrivée n'est pas déjà dans la liste
                        fermeture.append(arrivee)
            i += 1  # On passe à l'élément suivant dans la liste

        return fermeture


    # Complétion

    def est_complet(self):
        for ligne in range(len(self.table_transitions)):
            for colonne in range(len(self.table_transitions[ligne])):
                etat_actuel = self.table_transitions[ligne][colonne]
                if etat_actuel == " ":
                    return False
        return True

    def completer(self):
        Poubelle = 'P'
        Poubelle_ajouté = False

        for ligne in range(len(self.table_transitions)):
            for colonne in range(len(self.table_transitions[ligne])):
                if self.table_transitions[ligne][colonne] == " ":
                    if not Poubelle_ajouté:
                        self.etats.append(Poubelle)
                        for i in range(len(self.alphabets)):
                            self.transitions.append(Poubelle + ',' + self.alphabets[i] + ',' + Poubelle)
                        Poubelle_ajouté = True
                    self.transitions.append(self.etats[ligne] + ',' + self.alphabets[colonne] + ',' + Poubelle)

        self.table_transitions = self.construire_table_transitions()
        return

    # Détermination et complétion

    def determination_completion(self):
        self.determinisation()
        self.table_transitions = self.construire_table_transitions()
        self.completer()
        self.table_transitions = self.construire_table_transitions()
        return

    # Langage complémentaire

    def langage_complementaire(self):
        nouv_terminaux = []
        for etat in self.etats:
            if etat not in self.terminaux:
                nouv_terminaux.append(etat)

        self.terminaux = nouv_terminaux
        self.table_transitions = self.construire_table_transitions()
        return

    # Reconnaissance de mot

    def get_etat_cible(self,etat, symbole_courant):
        for transition in self.transitions:
            temp = transition.split(',')
            if temp[0] == etat and temp[1] == symbole_courant:
                return temp[2]
        return 'fin'

    def mot_reconnu(self, mot):
        etat_courant = self.initiaux[0]
        symbole_courant = mot[0] if len(mot) != 0 else ''
        cpt = 0
        while True:
            if cpt == len(mot):
                if etat_courant in self.terminaux:
                    return True
                else:
                    return False
            etat_cible = self.get_etat_cible(etat_courant, symbole_courant)

            if (etat_courant + ',' + symbole_courant + ',' + etat_cible) in self.transitions:
                etat_courant = etat_cible
                cpt = cpt + 1
                if cpt < len(mot):
                    symbole_courant = mot[cpt]
            else:
                return False
