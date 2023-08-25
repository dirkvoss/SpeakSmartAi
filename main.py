import openai

openai.api_key = "OPENAI_API_KEY"
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Wann war der 1 Weltkreig?"}])
response = chat_completion.choices[0].message["content"]
print(response)

