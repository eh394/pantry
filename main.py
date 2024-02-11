from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)











# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


# url = 'https://api.openai.com/v1/chat/completions'

# headers = {'Content-Type': 'application/json', 'Authorization': 
# f'Bearer {OPENAI_API_KEY}'}

# body = {'model': 'gpt-3.5-turbo', 'messages': [{'role': 'user', 'content': 'What is your name?'}]}


# x = requests.post(url, json = body, headers = headers)
# print(x.text)
