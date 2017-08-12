FROM python:3.6.2

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY app /app
COPY cmd.sh /
COPY uwsgi.ini /

WORKDIR /app

EXPOSE 9090 9191
USER uwsgi

CMD ["/cmd.sh"]