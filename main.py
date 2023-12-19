from pyscript import document
import json

results = []

def test(event):
    x = document.querySelector("#result")
    y = document.querySelector("#num-input")

    x.innerText = y.value

def getNumber():
    file = open("result.json", "r")
    data = json.load(file)

    for info in data["result"]:
        results.append(info)

    file.close()

getNumber()
print(results)