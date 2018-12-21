from flask import Flask, request
import json
import googleExport
import addToPatchSelenium
import os
import sys

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
  data = json.loads(request.data)
  emailAddress = data["user"]["emailAddress"]
  issue = data["issue"]["key"]
  itemsToAdd = googleExport.getValues(issue)
  #print(itemsToAdd, file=sys.stdout)
  addToPatchSelenium.run(itemsToAdd, issue, emailAddress)
  #print(request.data)
  return '', 200
   
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80, threaded=True)
