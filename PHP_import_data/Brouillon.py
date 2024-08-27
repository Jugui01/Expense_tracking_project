import pandas as pd
import sys
import os
import warnings

warnings.filterwarnings("ignore")

# Obtenir le chemin du fichier depuis les arguments de la ligne de commande
file_path = "D:\\Travail pro\\Github repo\\Expense_tracking_project\\Fichier brut exemple\\CA20240722_121002.xlsx"

# Fonction pour récupérer les données à partir de la ligne spécifiée d'un fichier Excel
def extract_data(file_path, n):
    try:
        # Lire le fichier Excel en commençant par la ligne spécifiée (index n)
        df = pd.read_excel(file_path, skiprows=n)
        # Merger colonnes Débit euros et Crédit euros
        df['montant'] = df['Débit euros'].fillna(df['Crédit euros'])
        df = df.drop(columns=['Débit euros', 'Crédit euros'])
        df['type_depense'] = None
        df = df[['Date','Libellé', 'type_depense','montant']]

        df.rename(columns={
            'Date': 'date_depense',
            'Libellé': 'libelle'
        }, inplace=True)
        # Sauvegarder le fichier Excel modifié
        df.to_excel("D:\\Travail pro\\Github repo\\Expense_tracking_project\\Fichier brut exemple\\test.xlsx", index=False)
    except Exception as e:
        print(f"Erreur lors de l'extraction des données : {e}", file=sys.stderr)

# Lire la cellule A9 pour vérifier si elle est non vide
def check_cell_a9(file_path):
    try:
        # Lire le fichier Excel en ne chargeant que les premières lignes nécessaires
        df = pd.read_excel(file_path, nrows=17)  # Lire les 9 premières lignes pour accéder à A9
        # Vérifier si la cellule A9 est non vide
        if df.iloc[8, 0] == "Date":  # Il est dans la 10ème ligne (index 9) et 1ère colonne (index 0)
            return True
    except Exception as e:
        print(f"Erreur lors de la vérification de la cellule A9 : {e}", file=sys.stderr)
    return False

#Appliquer la fonction appropriée en fonction de la valeur de la cellule A9
try:
    if check_cell_a9(file_path):
        extract_data(file_path, 9)
        print(f'La cellule A9 est non vide. Les données du fichier {file_path} ont été extraites à partir de la ligne 10.')
    else:
        extract_data(file_path, 16)
        print(f'La cellule A9 est vide. Les données du fichier {file_path} ont été extraites à partir de la ligne 17.')
except Exception as e:
    print(f"Erreur générale : {e}", file=sys.stderr)
