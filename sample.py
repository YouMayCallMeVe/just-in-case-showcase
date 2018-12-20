import json
import googleExport
import addToPatchSelenium
import os.path

def js_r(filename):
   with open(filename) as f_in:
       return(json.load(f_in))

if __name__ == "__main__":
    name = 'lock.txt'
    while(os.path.isfile(name)):
        time.sleep(10)
    f = open(name,'w')
    f.write('locked')
    f.close()
    data = js_r('sampleResponse.json')
    emailAddress = data["user"]["emailAddress"]
    issue = data["issue"]["key"]
    itemsToAdd = googleExport.getValues(issue)
    issue = "MR-1588"
    addToPatchSelenium.run(itemsToAdd, issue, emailAddress)
    os.remove(name)