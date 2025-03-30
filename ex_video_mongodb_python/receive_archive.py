from pymongo import MongoClient
import gridfs
from bson import ObjectId  # Importando ObjectId

# Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["bd_ex_video"]
fs = gridfs.GridFS(db)

diretorio = input('Em que diretório deseja baixar o vídeo?')

# Buscar o registro do video usando o file_id (ObjectId)
file_id = ObjectId(input('Qual o ID do video? '))

# Recuperar o video
file = fs.get(file_id)

# Salvar o video no seu computador
with open(f"{diretorio}/video_recuperado.mp4", "wb") as f:
    f.write(file.read())  # Escreve o conteúdo do video recuperado

print("Arquivo recuperado e salvo com sucesso!")