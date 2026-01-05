import json
data={
    "Name":"Gayathri",
    "Dept":"AI&DS"
}
with open("JsonData",'w') as f:
    json.dump(data,f,indent=5)
