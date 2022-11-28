from flask import Flask, request, redirect, render_template, session, url_for, Response
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('cover.html', home=True)

@app.route('/', methods=['POST'])
def post_content():
    print(request.files['file'])
    print(request.form['text-input'])
    return render_template('cover.html', home=True)

@app.route('/about', methods=['GET'])
def about_page():
    return render_template('cover.html', about=True)

@app.route('/samples', methods=['GET'])
def samples_page():
    return render_template('cover.html', samples=True)