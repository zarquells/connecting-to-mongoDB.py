from pymongo import MongoClient
import gridfs
import os

print(os.getcwd())
client = MongoClient('mongodb://localhost:27017/')
db = client['bd_ex_video']
fs = gridfs.GridFS(db)

directory = input('Qual o diretório do vídeo? ')
archive = input('Qual o nome do vídeo? Coloque a extensão, exemplo: .mp3, mp4 ')
archive_path = os.path.join(directory, archive)

with open(archive_path, 'rb') as f:
    file_id = fs.put(f, filename="video.mp4")

print("Arquivo enviado com ID:", file_id)