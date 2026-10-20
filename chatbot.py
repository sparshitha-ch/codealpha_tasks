
import random

responses = {
    "hello": ["Hi! How can I help you?", "Hello! Welcome!"],
    "how are you": ["I'm doing well! How are you?", "I'm fine, thank you!"],
    "your name": ["I'm CodeBot, your friendly chatbot!"],
    "help": ["You can say hello, ask my name, or ask how I am."],
    "bye": ["Goodbye! Have a great day!"]
}

def get_response(message):
    message = message.lower().strip()

    for keyword, replies in responses.items():
        if keyword in message:
            return random.choice(replies)

    return "Sorry, I don't understand. Type 'help' for suggestions."

print("Welcome to CodeBot!")
print("Type 'bye' to exit.")

while True:
    user_message = input("You: ")
    print("CodeBot:", get_response(user_message))

    if user_message.lower().strip() == "bye":
        break
 