FROM python:3.11

WORKDIR /controle_de_alugueis_backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "rental_system.wsgi:application"]

