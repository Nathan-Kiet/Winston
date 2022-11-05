import json

cNum = input("Class Number \n")
qNum = input("Quarter Number \n")
majOrMin = input("Major or Minor \n")
aNum = int(input("Assignment Number \n"))

with open("EX.Storage.json",'r+') as file:
    data = json.load(file)

print("----------")
print(data["C"+cNum]["Q"+qNum][majOrMin]["aName"][aNum])
print(data["C"+cNum]["Q"+qNum][majOrMin]["date"][aNum])
print(data["C"+cNum]["Q"+qNum][majOrMin]["gGrade"][aNum])
print(data["C"+cNum]["Q"+qNum][majOrMin]["fGrade"][aNum])
print(data["C"+cNum]["Q"+qNum][majOrMin]["redo"][aNum])
print("----------")