#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 23:26:08 2019

@author: easy

점수 입력 받은 후 등급 나누기
"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def score():
    return render_template('base.html')

@app.route('/result', methods=['POST'])
def result():
    
    if request.method == 'POST':
        score = request.form['grade'] #input의 name"이름"의 값 추출 
        score = int(score)
        
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        else:
            return "D"
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)