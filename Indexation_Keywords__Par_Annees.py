import pandas as pd

data_path = "/home/kylian/Documents/S5/SAE/IndexationsKeywords/data/cleaned_data.csv"

data = pd.read_csv(data_path)


titres_annees = data[["Title", "Year"]].values.tolist()

# On va créer une liste de mot pour chaque année
def lister_mot_par_annees():
    liste_mot_par_annnes = {}
    for title,year in titres_annees:
        if year not in liste_mot_par_annnes:
            liste_mot_par_annnes[year] = title
        else :
            liste_mot_par_annnes[year] += " " + str(title)
    return liste_mot_par_annnes

#print(lister_mot_par_annees())

#Crée un dictionnaire année -> list[mot : nb_occurrences] triée en croissant par an
def compter_occurence_mots():
    indexation = {}

    liste_mot_par_annees = lister_mot_par_annees()
    for year in liste_mot_par_annees:
        comptage = {}
        liste_mot = liste_mot_par_annees[year].split()
        for mot in liste_mot:
            comptage[mot] = liste_mot.count(mot)
        indexation[year] = comptage

    return dict(sorted(indexation.items())) # Tri par clé, soit par année

# Renvoie un dictionnaire trié par nombre d'occurence et par an croissant
def trier_dictionnaire_pour_chaque_annee_par_occurences_des_mots():
    indexation = compter_occurence_mots()
    #print(indexation_tri_annee[1949]) # Teste du dictionnaire non trié
    for cle in indexation:
        value_sort = dict(sorted(indexation[cle].items(), key=lambda item: item[1], reverse=True))
        indexation[cle] = value_sort

    return indexation

indexation = trier_dictionnaire_pour_chaque_annee_par_occurences_des_mots()

#print(indexation)

# Retourne la liste des mots et leur occurence pour une année donnée, trié par ordre décroissant de nb occurences.
def get_comptage_avec_annee(annee):
    return indexation[annee]

# liste_annees permet de boucler sur toutes les annees existantes avec les fonctions suivantes
# liste_annees = list(indexation.keys())
# for annee in liste_annees:
#     print(f"{annee} : {get_comptage_avec_annee(annee)}")


# Renvoie le mot le plus réccurent pour une année donnée
def get_mot_plus_reccurent_annee(annee):
    return next(iter(indexation[annee]))

#print(get_mot_plus_reccurent_annee(2022))

# Renvoie les n mots les plus réccurents pour une annee n
def get_top_n_mots_plus_reccurent_annee(n,annee):
    while(n > len(get_comptage_avec_annee(annee))):
        n -= 1
    top = {}
    mots_et_occurrences = get_comptage_avec_annee(annee)
    keys = list(get_comptage_avec_annee(annee).keys())
    for i in range(0,n):
        mot = keys[i]
        top[mot] = mots_et_occurrences[mot]
    return top


#print(get_top_n_mots_plus_reccurent_annee(5,1992))

# Ecris les mots les plus récurrents pour chaque année avec n le nombre de mots
def ecrire_tendances_toutes_les_annees(n):
    liste_annees = list(indexation.keys())
    with open("./data/mots_top1.txt", "w") as fichier:
        print("Voici la liste de chaque mot le plus réccurent par année",file=fichier)
        for annee in liste_annees:
            print(f"{annee} : {get_top_n_mots_plus_reccurent_annee(n,annee)}",file=fichier)

ecrire_tendances_toutes_les_annees(5)


