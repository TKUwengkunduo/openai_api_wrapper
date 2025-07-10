from client import OpenAIClient

# 使用 gpt-3.5-turbo，回應更隨機
client = OpenAIClient(model="gpt-3.5-turbo", temperature=0.9)

resp = client.chat_completion(
    [
        {"role": "system", "content": "你是詩人，回答要押韻。"},
        {"role": "user",   "content": "寫一首關於夏天的四行詩。"}
    ],
    max_tokens=60
)
print(resp.choices[0].message.content)
