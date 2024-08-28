import pandas as pd
import sys
import os
import warnings
import yaml
from sqlalchemy import create_engine


def connect_mysql(config_path):

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    db_config = config['database']
    user = db_config['user']
    password = db_config['password']
    host = db_config['host']
    port = db_config['port']
    database = db_config['name']
    return user, password, host, port, database


# Fonction pour récupérer les données à partir de la ligne spécifiée d'un fichier Excel
def extract_data(config_path, file_path, file_name, n):
    try:
        user, password, host, port, database = connect_mysql(config_path)

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

            df['date_depense'] = pd.to_datetime(df['date_depense'], errors='coerce')
            df['libelle'] = df['libelle'].str[:25]
            

            ###Inclure dans la base mysql, table depenses
            # Créer l'URL de connexion pour SQLAlchemy
            mariadb_url = f"mariadb+mariadbconnector://{user}:{password}@{host}:{port}/{database}"

            # Créer l'objet engine pour la connexion
            engine = create_engine(mariadb_url)

            table_name_depenses = 'depenses'
            table_name_file_name = 'file_name'

            try:
                df.to_sql(table_name_depenses, con=engine, if_exists='append', index=False)
                print("Insertion réussie !")
            except Exception as e:
                print(f"Une erreur s'est produite lors de l'insertion : {e}")
                
            ###Inclure dans la base mysql nom de fichier dans table file_name
            df_file_name = pd.DataFrame({
                'Name': [file_name]  # La colonne 'file_name' doit exister dans la table
            })

            try:
                df_file_name.to_sql(table_name_file_name, con=engine, if_exists='append', index=False)
                print("Insertion dans 'file_name' réussie !")
            except Exception as e:
                print(f"Une erreur s'est produite lors de l'insertion dans 'file_name' : {e}")


        except Exception as e:
            print(f"Erreur lors de l'extraction des données : {e}", file=sys.stderr)

    except Exception as e:
        print(f"Erreur lors de l'extraction des informations de configuration BDD : {e}", file=sys.stderr)




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







