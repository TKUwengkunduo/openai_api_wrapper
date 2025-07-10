from openai_client import OpenAIClient

client = OpenAIClient()

messages = [
    {"role": "system", "content": "你是一個友善的助手。"},
    {"role": "user",   "content": "你好"}
]

resp = client.chat_completion(messages)
print(resp.choices[0].message.content)
