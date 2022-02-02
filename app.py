from flask import Flask
app = Flask(__name__)
 
@app.route('/hello')
def hello():
    return 'Ajith Sivadas - 1001829098'
 
#app.run(host='localhost', port=5000)
