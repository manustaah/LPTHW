from flask import flask

app= Flask(__name__)

@app.route('/hello')
def root_page():
    response = render_template('hello.html', greeting="Hola, Jon")"""
    
    return response

if __name__ == "__main__"
    app.run()#start flask
