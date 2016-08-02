from flask import Flask
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
default_name = "Enes Anbar"


@app.route('/')
def get_indenticon():
    name = default_name

    template_env = Environment(loader = FileSystemLoader(searchpath = "."))
    template = template_env.get_template("index.html")

    return template.render({'name': name})

# executes when the file is called as a standalone program and
# not when running as part of a larger application.
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
