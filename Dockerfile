# Usar a imagem oficial do Python
FROM python:3.11

# Definir o diretório de trabalho dentro do container
WORKDIR /api

# Copiar os arquivos do projeto para o container
COPY ./api .
COPY requirements.txt .

# Instala as dependencias do projeto
RUN pip3 install -r requirements.txt

# Porta usada
EXPOSE 5500

# Executar a API Flask
CMD ["python3", "app.py"]
