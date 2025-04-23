from flask import Flask, render_template
from parser.log_parser import scan_log

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Scan the sample log file
    log_file = 'samples/apache_log_sample.txt'
    threats = scan_log(log_file)
    return render_template('dashboard.html', threats=threats)

if __name__ == '__main__':
    app.run(debug=True)
