FROM python:3.7.10-slim-stretch

WORKDIR /app 

COPY requirements.txt .

RUN pip3 install -r requirements.txt 
RUN pip3 install psycopg2

COPY . .

ENV FLASK_APP run.py

# ENTRYPOINT ["python3"] 

# CMD ["run.py"]