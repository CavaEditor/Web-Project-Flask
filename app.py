from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route('/about')
def about():
    return "About page"

if __name__ == "__main__":
    app.run(debug=True)