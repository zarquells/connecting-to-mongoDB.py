from pymongo import MongoClient
import gridfs
import datetime
import os

client = MongoClient('mongodb://localhost:27017/')
db     = client['bd_ex_music']
schema = db['musics']
fs = gridfs.GridFS(db)

global file_id

def insert_music():
    try:
        directory = input('Qual o diretório da(s) música(s)? ')
        archive = input('Qual o nome da música? Coloque a extensão, exemplo: .mp3, mp4')
        archive_path = os.path.join(directory, archive)
        
        with open(archive_path, 'rb') as f:
            file_id = fs.put(f, filename=f'{archive}')

        print("Arquivo enviado com ID:", file_id)
        return True
    except Exception:
        return False

def insert_info_music():
    try:
        name = input('Qual o nome da música? ')
        type = input('Qual o tipo de arquivo? ')
        description = input('Qual a descrição? ')
        date = datetime.datetime.now() 
        keywords = input('Quais tags? Separe por espaço ').split()
        favorite = input('É seu favorito? ')

        infos = {
            'Titulo': name, 
            'Tipo': type, 
            'descricao': description, 
            'data_adicao': date, 
            'tags': keywords, 
            'favorito': favorite, 
            'ID da música': file_id
        }

        insert = schema.insert_one(infos)
        print(f'Arquivo armazenado na biblioteca: {insert}')
        return True
    except Exception:
        return False

first = int(input('Quantas músicas quer inserir? '))
for i in range(first):
    if insert_music():
        insert_info_music()
    else:
        print('Algo deu errado')
        break