import nltk
from nltk.chat.util import Chat, reflections

# Define the patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you|how\'s it going', ['I\'m just a bot, but I\'m doing well!', 'I\'m here to help!']),
    (r'what is your name|who are you', ['I\'m a chatbot called ChatGPT.', 'You can call me ChatGPT.']),
    (r'bye|goodbye', ['Goodbye!', 'Have a great day!', 'See you later!'])
]

# Create the chatbot
chatbot = Chat(patterns, reflections)

# Main loop for chatting
print("Chatbot: Hi! I'm Ghost. How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
