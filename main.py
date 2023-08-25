import openai

openai.api_key = "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"
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Wann war der 1 Weltkreig?"}])
response = chat_completion.choices[0].message["content"]
print(response)

