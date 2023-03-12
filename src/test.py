import openai
import os

openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model = 'gpt-3.5-turbo',
  messages = [
    {'role': 'user', 'content': 'Hello!'}
  ],
  temperature = 0  
)

print(completion['choices'][0]['message']['content'])