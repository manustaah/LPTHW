from flask import Flask
from flask import render_template. request

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get('name')
    greeting = "Hello, %s!" % name
    return render_template('index.html'. greet=greeting)

if __name__ == "__main__":
    app.run()
