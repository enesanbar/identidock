from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# executes when the file is called as a standalone program and
# not when running as part of a larger application.
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
