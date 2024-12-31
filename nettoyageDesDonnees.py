import nltk
import pandas as pd
import re
from nltk.corpus import stopwords

data_path = "/home/kylian/Documents/S5/SAE/IndexationsKeywords/data/master_dbo_dblp2_2.csv"

# Chargement complet
data = pd.read_csv(data_path)

# Chargement limité
data = pd.read_csv(data_path,nrows=100000,header=None)
print(data.columns)

# Ajouter titres
columns = ['Title','Year']
data.columns = columns


titres_annees = data[["Title", "Year"]].values.tolist()


# On retire tout caractères autres que alphanumériques
titres_annees = [[re.sub(r'[^\w\s]', '', str(element[0])), element[1]] for element in titres_annees]


# Gestion des stop words

nltk.download('stopwords')
stopwords_en = set(stopwords.words('english'))
stopwords_fr = set(stopwords.words('french'))
stopwords_de = set(stopwords.words('german'))
stopwords_es = set(stopwords.words('spanish'))
stopwords_it = set(stopwords.words('italian'))
stopwords_po = set(stopwords.words('portuguese'))


stopwords_all = stopwords_en.union(stopwords_fr).union(stopwords_de).union(stopwords_es).union(stopwords_it).union(stopwords_po)

def remove_stopwords(text):
    # On nettoie les texte et garde que les mots
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    filtered_words = [word for word in words if word not in stopwords_all]
    return ' '.join(filtered_words)





# Conversion en DataFrame
df = pd.DataFrame(titres_annees, columns=['Title','Year'])

df['Title'] = df['Title'].apply(remove_stopwords)

# Sauvegarde dans un nouveau fichier CSV
output_path = "/home/kylian/Documents/S5/SAE/IndexationsKeywords/data/cleaned_data.csv"
df.to_csv(output_path, index=False)
