FROM python:3.6

# Create the uwsgi user and group
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi

COPY app /app
COPY cmd.sh /
COPY requirements.txt /
COPY uwsgi.ini /

RUN pip install -r requirements.txt
WORKDIR /app

EXPOSE 9090 9191
USER uwsgi

CMD ["/cmd.sh"]