from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    print("Files in %r: %s" % (cwd, files))
    with open('app/currentHosts.txt', 'r') as f: #indicate the path of the file
        hosts = [iterator.strip() for iterator in f]
            
    return render_template('index.html', title='Monitoring Network', hosts=hosts)
