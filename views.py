from flask import Flask, request, redirect, render_template, session, url_for, Response
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1000 * 1000

@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>')
def homepage(path):
    return render_template('index.html', home=True)

@app.route('/', methods=['POST'])
def homepage_post_content():
    received_file = request.files['file']
    filename = secure_filename(received_file.filename)
    received_text = str(request.form['text-input'])
    return render_template('index.html', home=True, submitted=True, filename=filename, text=received_text)

@app.route('/about', methods=['GET'])
def about_page():
    return render_template('index.html', about=True)

@app.route('/samples', methods=['GET'])
def samples_page():
    return render_template('index.html', samples=True)

@app.route('/samples', methods=['POST'])
def samples_post_content():
    record_type = str(request.form['record_type'])
    file_format = str(request.form['file_format'])
    record_qty = int(request.form['record_qty'])
    print(record_type, record_qty, file_format)
    return render_template('index.html', samples=True)

