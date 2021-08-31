FROM python:3.6
RUN apt-get update && apt-get install -y ffmpeg

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
