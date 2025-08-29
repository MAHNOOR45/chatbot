import requests

# 🔑 Yahan apni DeepSeek API key dalni hai
API_KEY = "your_deepseek_api_key_here"

# API endpoint
url = "https://api.deepseek.com/v1/chat/completions"

def faq_agent(question):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",   # DeepSeek ka model name
        "messages": [
            {"role": "system", "content": "You are a helpful FAQ bot."},
            {"role": "user", "content": question}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"


# Console chatbot loop
if __name__ == "__main__":
    print("🤖 FAQBot is running! (type 'exit' to quit)\n")
    while True:
        user_q = input("You: ")
        if user_q.lower().strip() in ["exit", "quit"]:
            print("FAQBot: Bye! 👋")
            break
        answer = faq_agent(user_q)
        print("FAQBot:", answer)
