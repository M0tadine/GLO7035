FROM python:3.7-alpine
RUN apt−get −y update
RUN apt−get install −y pip3 build−essential
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
EXPOSE 5000
RUN wget https://www.donneesquebec.ca/recherche/dataset/8dba5a63-49b2-4d20-8333-f99df764ce10/resource/57064f57-122c-4e45-894e-a4dcf39ce6fa/download/vdq-reseaucyclable.geojson
RUN python3 initMongoDb.py
RUN python3 app.py
