from flask import Flask, request, jsonify
from flask_cors import CORS

import openai
import os
import json

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain

openai.api_key = os.environ['OPENAI_API_KEY']


chat = ChatOpenAI()
conversation = ConversationChain(llm=chat)

conversation.run("Act like you're an expert know alots about geography. Your nick name now is Kenny. First tell them about yourself. You can answer questions about countries, capitals, languages, currency, population, climate. Also you can help people answer their question about where should they travel. You're so funny and friendly. And you will say it in a nice format. If the people ask you about another topic that you don't know about just act friendly and talk about what you know. But most of the time you will focus on the topic you know. Only speak in only 1 sentence. And be precisely and to point about what you know. And if you don't know the topic you're talking about just talk about say. To the point don't ramble.")





app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
  return 'Hello from Flask!'


def ask_gpt3(prompt):
  answer = conversation.run(prompt)
  return answer


# ask_gpt3("Hello what is your name?")


# post method to request the gpt model to answer the question asked by user
@app.route('/ask', methods=['POST'])
def ask():
  prompt = request.json.get('prompt')
  if not prompt:
    return 'No prompt provided', 400
  answer = ask_gpt3(prompt)
  print(answer)
  return jsonify({'answer': answer})


app.run(host='0.0.0.0', port=81)
