import pandas as pd
import sys
import os
import warnings
import yaml
from sqlalchemy import create_engine
from modify_excel import connect_mysql, extract_data, check_cell_a9

warnings.filterwarnings("ignore")

# Vérification du nombre d'arguments
if len(sys.argv) != 4:
    print("Usage: python main.py <file_path> <config_path> <file_name>", file=sys.stderr)
    sys.exit(1)

file_path = sys.argv[1]
config_path = sys.argv[2]
file_name = sys.argv[3]

# Vérification de l'existence des fichiers
if not os.path.exists(file_path):
    print(f"Erreur: Le fichier {file_path} n'existe pas.", file=sys.stderr)
    sys.exit(1)

if not os.path.exists(config_path):
    print(f"Erreur: Le fichier de configuration {config_path} n'existe pas.", file=sys.stderr)
    sys.exit(1)

# Appliquer la fonction appropriée en fonction de la valeur de la cellule A9
try:
    if check_cell_a9(file_path):
        extract_data(config_path, file_path, file_name, 9)
        print(f'La cellule A9 est non vide. Les données du fichier {file_path} ont été extraites à partir de la ligne 10.')
    else:
        extract_data(config_path, file_path, file_name, 16)
        print(f'La cellule A9 est vide. Les données du fichier {file_path} ont été extraites à partir de la ligne 17.')
except Exception as e:
    print(f"Erreur lors de l'exécution du traitement : {e}", file=sys.stderr)
    sys.exit(1)
