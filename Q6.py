sampleDict = {

  "name": "Kelly",

  "age":25,

  "salary": 8000,

  "city": "New york"

}
print("before",sampleDict)
sampleDict["location"]=sampleDict.pop("city")
print("after",sampleDict)
