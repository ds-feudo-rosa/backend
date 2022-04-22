FROM python:3.10

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "src/manage.py", "run", "-h", "0.0.0.0"]

