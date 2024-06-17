# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos para o contêiner
COPY app.py .
COPY requirements.txt .

# Instale as dependências
RUN pip install -r requirements.txt

# Exponha a porta usada pelo Flask
EXPOSE 5001

# Comando para rodar a aplicação
CMD ["python", "app.py"]
