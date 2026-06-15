faq = {
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is python": "Python is a programming language.",
    "what is machine learning": "Machine Learning enables computers to learn from data.",
    "who are you": "I am a FAQ Chatbot."
}

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Goodbye!")
        break

    if user in faq:
        print("Bot:", faq[user])
    else:
        print("Bot: Sorry, I don't know that answer.")