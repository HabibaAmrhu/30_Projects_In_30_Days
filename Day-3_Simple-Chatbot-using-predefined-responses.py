import re

# dictionary of responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm a chatbot created to assist you.",
    "help": "Sure, I'm here to help. What do you need assistance with?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! I'm happy to help.",
    "default": "I'm not sure I understand. Could you please rephrase?"
}

# function to find response
def chat_res(user_input):
    user_input = user_input.lower()
    for keyword in responses:
        if re.search(keyword, user_input):
            return responses[keyword]
    return responses["default"]

# main chatbot function
def chatbot():
    print("Chatbot: Hello! I'm here to assist you. (type 'bye' to exit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = chat_res(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()
