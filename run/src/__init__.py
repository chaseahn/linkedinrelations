#!/usr/bin/env python3


import os

from flask import Flask, render_template, request, url_for, redirect, session

from .controllers.private import pichu as private_app
from .models.model import *

pikachu = Flask(__name__)

pikachu.register_blueprint(public_buzz)
pikachu.register_blueprint(private_buzz)


@electabuzz.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('public/index.html')
    elif request.method == 'POST':
        if request.form['post_button'] == 'Login':
            """ 
            --------------------
                    LOGIN
            --------------------
            """
            try:
                with User(username=request.form['username'], password=request.form['password']) as un:
                    if un.login(request.form['password']):
                        session['username'] = un.username
                        session['pk'] = un.pk
                        session['age'] = un.age
                        session['gender'] = un.gender
                        return redirect('p/adex')
                    else:
                        return redirect('/', message='Username/Password not recognized...try again!')
            except TypeError:
                return render_template('public/index-vk.html', message="Are you sure that's correct?")
        else:
            search_terms = request.form['post_button']
            return redirect('/search/'+search_terms)
    else:
        pass
