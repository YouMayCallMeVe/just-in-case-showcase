from flask import Flask, request
import json
import googleExport
import addToPatchSelenium

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
  name = 'lock.txt'
  while(os.path.isfile(name)):
      time.sleep(10)
  f = open(name,'w')
  f.write('locked')
  f.close()
  data = json.loads(request.data)
  emailAddress = data["user"]["emailAddress"]
  issue = data["issue"]["key"]
  itemsToAdd = googleExport.getValues(issue)
  issue = "MR-1794"
  addToPatchSelenium.run(itemsToAdd, issue, emailAddress)
  os.remove(name)

if __name__ == '__main__':
   app.run(processes=4)
