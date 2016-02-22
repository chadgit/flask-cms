"""
Routes and views for the flask application.
"""
import os
from os import path
from datetime import datetime
from flask import render_template
from flaskCMS import app

def make_tree(path):
    tree = dict(name=os.path.basename(path), children=[])
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree['children'].append(make_tree(fn))
            else:
                tree['children'].append(dict(name=name))
    return tree

@app.route('/editors/json', defaults={'path': 'json_editors.html'})
@app.route('/editors/json/<path:path>')
def dirtree(path):
    #path = os.path.expanduser(u'~')
    print path
    json_files = "\\templates\\tools\\editors\\jsoneditor-master\\"
    _path = os.path.abspath(__package__) + json_files

    return render_template("json_editor.html", tree=make_tree(_path), include_list = "./tools/editors/jsoneditor-master/"+path)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
