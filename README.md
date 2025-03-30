# Gerenciador de Arquivos .mp3 com MongoDB e GridFS

Este projeto permite armazenar arquivos .mp3 no MongoDB utilizando GridFS.

## Requisitos

- Python 3.13.2
- MongoDB instalado e em execução
- Biblioteca `pymongo` instalada
- Visual Studio Code

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/zarquells/connecting-to-mongoDB.py
   cd connecting-to-mongoDB.py
   ```
2. Instale as dependências:
   ```bash
   pip install pymongo
   ```

## Problemas Conhecidos

- O script pode falhar caso o caminho do arquivo esteja incorreto.