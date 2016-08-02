from flask import Flask, Response
from jinja2 import Environment, FileSystemLoader
import requests

app = Flask(__name__)
default_name = "Enes Anbar"


@app.route('/')
def main_page():
    name = default_name

    template_env = Environment(loader = FileSystemLoader(searchpath = "."))
    template = template_env.get_template("index.html")

    return template.render({'name': name})


@app.route('/monster/<name>')
def get_identicon(name):
    r = requests.get('http://dnmonster:8080/monster/{}?size=80'.format(name))
    image = r.content

    return Response(image, mimetype = 'image/png')

# executes when the file is called as a standalone program and
# not when running as part of a larger application.
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
