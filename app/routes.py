from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    hosts = [
            {'IP': 'Hosts example 0'},
            {'IP': 'Hosts example 1'},
            {'IP': 'Hosts example 2'},
            {'IP': 'Hosts example 3'}
            ]
    return render_template('index.html', title='Monitoring Network', hosts=hosts)
