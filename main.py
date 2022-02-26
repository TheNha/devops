from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return 'My DevOps is here! Hello World!!!'

if __name__ == '__main__':
    app.run(host="0.0.0.0")