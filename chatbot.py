import nltk
from nltk.chat.util import Chat, reflections
# Define chatbot patterns (pairs of regex and responses)
pairs = [
[
r"my name is (.*)",
["Hello %1, how can I help you today?", "Nice to meet you %1!"]
],
[
r"hi|hello|hey",
["Hello!", "Hi there!", "Hey! How can I assist you?"]
],
[
r"what is your name\??",
["I am a Python-powered chatbot."]
],
[
r"how are you\??",
["I'm doing well, thank you!", "All good here. What about you?"]
],
[
r"(.*) your name\??",
["I go by many names, but you can call me ChatBot."]
],
[
r"quit",
["Goodbye! Have a great day!"]
],
[
r"(.*)",
["Sorry, I didn't understand that. Can you rephrase?"]
]
]
def start_chat():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
     
chatbot = Chat(pairs, reflections)
chatbot.converse()
if "name" == "main":
    start_chat()