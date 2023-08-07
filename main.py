from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('/index.html')

@app.route('/cyberbullying')
def cb():
    return render_template('/cyberbullying.html')

@app.route('/identitytheft')
def it():
    return render_template('/identitytheft.html')

@app.route('/cybersecurity')
def cs():
    return render_template('/cybersecurity.html')

