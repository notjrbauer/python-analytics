FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# ENV vars
ENV PORT=4000
ENTRYPOINT ["python"]
CMD ["index.py"]
