#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 01:29:01 2019

@author: easy

단어를 입력받아 영문자 변환하는 기능
소문자 > 대문자
대문자 > 소문자
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/result', methods=['POST'])
def result():
    
    if request.method == 'POST':
        word = request.form['word'] #input의 name="이름"의 값 추출
        
    if word == word.upper():
        return word.lower()
    else:
        return word.upper()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)