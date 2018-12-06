from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
   data = json.loads(request.data)
   emailAddress = data["user"]["emailAddress"]
   issue = data["issue"]["key"]

if __name__ == '__main__':
   app.run()