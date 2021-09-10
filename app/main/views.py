from . import main
from .. import db 
from ..models import Alias
from flask import render_template, redirect, url_for, request

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        alias = request.form.get('alias')
        a = Alias(alias=alias, url=url)
        try:
            db.session.add(a)
            db.session.commit()
        except Exception as e:
            return render_template('index.html')
    return render_template('index.html')