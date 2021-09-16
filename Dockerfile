FROM python:3.8.7

WORKDIR /assign1

COPY . .

RUN pip install -r requirements.txt

CMD ["python","main.py"]