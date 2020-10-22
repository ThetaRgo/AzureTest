#!/usr/bin/env python
# encoding:utf-8
# @Time   : 2020/10/22
# @Author : humaohai
# @File   : app.py.py
# @desc   : 


from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'





if __name__ == '__main__':
    app.run(debug=True)