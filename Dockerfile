FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1  
ENV PYTHONUNBUFFERED 1  

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]