'''
Created on 12 de jun de 2018

@author: jeanm
'''

from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route('/')
def hello_world():
    return 'Hello, World!'
