FROM python:3.10-buster

WORKDIR /project

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app/App.py"]
