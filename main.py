from pyscript import document
import json

data = {
    "result":
    [
        ["921688"],
        ["903444"],
        ["816183","902479","876088","979810"],
        ["928285","992154"],
        ["836094","889499","860003","900376","860946","911575","863811","980565","872941","995690"]
    ]
}

results = []

def test(event):
    x = document.querySelector("#result")
    y = document.querySelector("#num-input")

    x.innerText = y.value

def get_number():
    for info in data["result"]:
        results.append(info)

def check_user_input(event):
    user_input = document.querySelector("#num-input")
    result_text = document.querySelector("#result")

    _input = user_input.value

    if len(_input) != 6:
        result_text.innerText = "Invalid Input"
        return

    for i in range(5):
        for j in results[i]:
            if _input == j:
                result_text.innerText = f"ถูกรางวัลที่ {i+1}"
                return
    result_text.innerText = "ไม่ถูกรางวัล"

get_number()