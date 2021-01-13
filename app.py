from flask import Flask, request, jsonify, render_template, Response, redirect, url_for, session

app = Flask(__name__)

app.secret_key ='13464846313211325f3e1a3sda16ae5r3afa16e'

@app.route('/')
def inicio(): 
    
    return "aqui estoy"

if __name__ == '__main__':
    app.run(debug=True)
