FROM python:3.10.0a7

WORKDIR /simple_server

COPY . .


ENV PORT=7777

EXPOSE 7777

CMD [ "python", "server.py"]