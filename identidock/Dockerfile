FROM python:3.6

# Create the uwsgi user and group
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi

COPY requirements.txt /
RUN pip install -r ./requirements.txt
COPY app /app
WORKDIR /app

EXPOSE 9090 9191
USER uwsgi

CMD ["uwsgi", "--http", "0.0.0.0:9090", "--wsgi-file", "/app/identidock.py", \
     "--callable", "app", "--stats", "0.0.0.0:9191"]