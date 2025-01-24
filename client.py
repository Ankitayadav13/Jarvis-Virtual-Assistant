from openai import OpenAI


#pip install openai
#default to getting the key using os.environ.get("OPENAI_API_KEY")
#if you saved the key under a different environment variable variable name, you can do something like:

client = OpenAI (
  api_key="c3b09a472fb04f0ba2453b4a67e9dc2d",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
   {"role":"system","content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
   {"role": "user","content":"what is coding"}
  ]
)

print(completion.choices[0].message.content)