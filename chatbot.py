print("="*50)
print("Welcome to Rule-Based AI Chatbot")
name=input("Enter your name: ")
while True:
    user=input(f"{name}: ").lower().strip()
    if user in ("hi","hello"):
        print("Bot: Hello! How can I help you?")
    elif user=="how are you":
        print("Bot: I am fine. Thank you!")
    elif user=="ai":
        print("Bot: AI stands for Artificial Intelligence.")
    elif user=="python":
        print("Bot: Python is a programming language.")
    elif user in ("thanks","thank you"):
        print("Bot: You're welcome!")
    elif user in ("bye","exit"):
        print(f"Bot: Goodbye {name}!")
        break
    else:
        print("Bot: Sorry! I don't understand.")
