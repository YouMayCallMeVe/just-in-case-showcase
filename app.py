from flask import Flask, request
import json
import googleExport
import addToPatchSeleniu

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
  data = json.loads(request.data)
  emailAddress = data["user"]["emailAddress"]
  issue = data["issue"]["key"]
  components = googleExport.getValues()
  issue = "MR-1794"
  itemsToAdd = []
  for row in components:
    if row[1] == issue:
      itemsToAdd.append(row[0])
  addToPatchSelenium.run(itemsToAdd, issue)

if __name__ == '__main__':
   app.run()