import json
import googleExport
import addToPatchSelenium

def js_r(filename):
   with open(filename) as f_in:
       return(json.load(f_in))

if __name__ == "__main__":
    data = js_r('sampleResponse.json')
    emailAddress = data["user"]["emailAddress"]
    issue = data["issue"]["key"]
    components = googleExport.getValues()
    issue = "MR-1794"
    itemsToAdd = []
    for row in components:
    	if row[1] == issue:
    		itemsToAdd.append(row[0])
    addToPatchSelenium.run(itemsToAdd, issue)
