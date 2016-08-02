from flask import Flask, Response, request
from jinja2 import Environment, FileSystemLoader
import requests
import hashlib
import redis

app = Flask(__name__)

cache = redis.StrictRedis(host = 'redis', port = 6379, db = 0)
default_name = "Enes Anbar"
salt = "UNIQUE_SALT"


@app.route('/', methods = ['GET', 'POST'])
def main_page():
    name = default_name

    if request.method == 'POST':
        name = request.form['name']

    # to generate different identicons for the same input in different sites
    salted_name = salt + name
    name_hash = hashlib.sha256(salted_name.encode()).hexdigest()

    template_env = Environment(loader = FileSystemLoader(searchpath = "."))
    template = template_env.get_template("index.html")

    return template.render({
        'name': name,
        'name_hash': name_hash
    })


@app.route('/monster/<name>')
def get_identicon(name):
    image = cache.get(name)
    if image is None:
        print("Cache miss", flush = True)
        r = requests.get('http://dnmonster:8080/monster/{}?size=80'.format(name))
        image = r.content
        cache.set(name, image)

    return Response(image, mimetype = 'image/png')

# executes when the file is called as a standalone program and
# not when running as part of a larger application.
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
