from openai import OpenAI
client = OpenAI(
  api_key="{API_KEY"}
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
