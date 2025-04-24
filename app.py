import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from parser.log_parser import scan_log

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'log'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    threats = []

    if request.method == 'POST':
        if 'logfile' not in request.files:
            return redirect(request.url)

        file = request.files['logfile']
        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            threats = scan_log(filepath)

    return render_template('dashboard.html', threats=threats)

if __name__ == '__main__':
    app.run(debug=True)
