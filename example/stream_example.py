from client import OpenAIClient

client = OpenAIClient()

# 開啟 streaming，逐步印出 token
stream = client.chat_completion(
    [
        {"role": "system", "content": "你是詩人，回答要押韻。"},
        {"role": "user",   "content": "寫一首關於夏天的四行詩。"}
    ],
    stream=True
)

for chunk in stream:
    print(chunk.choices[0].delta.get("content", ""), end="")
