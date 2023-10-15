  
FROM python:3.9

RUN mkdir /app
WORKDIR /app

RUN apt update && \
    apt install -y postgresql-client

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Specify the command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002", "--reload"]
