import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created using NLTK.", "You can call me NLTK Bot!"]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?", "I’m great! Thanks for asking."]
    ],
    [
        r"sorry (.*)",
        ["It's okay.", "No problem at all."]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "Glad to hear you're doing well!"]
    ],
    [
        r"bye|exit",
        ["Goodbye!", "See you later!", "Bye! Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase that?", "Interesting... Tell me more!"]
    ]
]

def nltk_chatbot():
    print("Hi! I'm a chatbot. Type 'bye' if you wish to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

nltk_chatbot()

