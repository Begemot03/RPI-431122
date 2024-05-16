from flask import Flask, render_template, request
from time import sleep

import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/answer")
def answer():
    prompt_data = {
        "modelUri": "gpt://b1gpja8hn3udbg3fku7j/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.2,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты консультант продажи ПО по отслеживанию авио рейсов"
            },
            {
                "role": "user",
                "text": request.args["q"]
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVN1plATldQj1focXhdN0JYhEsnTWUTYNR2Mlhn"
    }
    
    try:
        response = requests.post(url, headers=headers, json=prompt_data)

        result_json = response.json()
        result_text = result_json['result']['alternatives'][0]['message']['text']

        return { "msg" : result_text }
    except:
        return { "msg" : "Произошла ошибка во время запроса" }

# ajemj504slqghtbugsbo

app.run()