# syntax=docker/dockerfile:1
FROM python:3.7
RUN apt-get  update
RUN apt-get install  -y python3-pip build-essential
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 80
RUN wget https://www.donneesquebec.ca/recherche/dataset/8dba5a63-49b2-4d20-8333-f99df764ce10/resource/57064f57-122c-4e45-894e-a4dcf39ce6fa/download/vdq-reseaucyclable.geojson
CMD ["python3","app.py"]
