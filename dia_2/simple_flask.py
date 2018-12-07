from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/sum/<a>/<b>")
def sum(a,b):
    return str(int(a)+int(b))

@app.route("/operations",methods=['POST'])
def operations():
    a,b = request.json['a'], request.json['b']
    return json.dumps({"mais": a+b,
                       "menos":a-b,
                       "vezes":a*b,
                       "dividido":a/b})

if __name__ == '__main__':
    app.run(port=5000)
