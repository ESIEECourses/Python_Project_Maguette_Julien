# dataReader.py
import shutil
import requests
import os

#récupération des données
def download_data():
    csv_url = "https://www.data.gouv.fr/fr/datasets/r/d3a98a30-893f-47f7-96c5-2f4bcaaa0d71"
    local_directory = os.getcwd()
    local_csv_filename = "donnéesCovid-fra.csv"
    local_csv_path = os.path.join(local_directory, local_csv_filename)

    response = requests.get(csv_url, stream=True)
    with open(local_csv_path, 'wb') as local_file:
        local_file.write(response.content)  # Utilisation de response.content pour écrire en mode binaire

    return local_csv_filename
