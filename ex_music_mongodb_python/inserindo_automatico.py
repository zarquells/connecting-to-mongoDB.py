from pymongo import MongoClient
import gridfs
import os

client = MongoClient('mongodb://localhost:27017/')
db     = client['bd_ex_music1']
schema = db['musics']
fs = gridfs.GridFS(db)

global musics
global ids_musics

ids_musics = []

def insert_musics():
    directory = input('Qual o diretório das músicas')
    musics = os.listdir(directory)
    try:
        for music in musics:
            music_path = os.path.join(directory, music)

            with open(music_path, 'rb') as f:
                file_id = fs.put(f, filename=f'{music}')

            ids_musics.append(file_id)
            print(f'Arquivo {music} enviado com o ID: {file_id}', )
        return True
    except Exception:
        return False

if insert_musics():
    print(f'Musicas armazenadas com sucesso! \nSegue array dos IDs: \n{ids_musics}')
else:
    print('Algo deu errado ao armazenar músicas, verifique o caminho dos arquivos.')