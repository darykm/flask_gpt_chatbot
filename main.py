import json
import os

import openai
from flask import Flask, render_template, request, jsonify
from openai import OpenAI


app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpt4', methods=['GET', 'POST'])
def gpt4():
    user_input = request.args.get('user_input') if request.method == 'GET' else request.form['user_input']
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ],
        model="gpt-3.5-turbo",
    )
    content = chat_completion.choices[0].message["content"]


    # try:

    # except openai.RateLimitError:
    #     content = "The server is experiencing a high volume of requests. Please try again later."

    return jsonify(content=content)

if __name__ == '__main__':
    app.run(debug=True)
