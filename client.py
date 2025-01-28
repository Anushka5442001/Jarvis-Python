from openai import OpenAI
client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  store=True,
  messages=[
    {"role": "system", "content": "You area virtual assistance named Jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "Write a haiku about ai"}
  ]
)

print(completion.choices[0].message.content);



#pip install openai