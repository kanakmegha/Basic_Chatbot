import nltk
from nltk.chat.util import Chat, reflections

# Define pairs for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that!", "Alright, great!"]
    ],
    [
        r"what is your favorite color?",
        ["My favorite color is blue.",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Can you please rephrase?",]
    ]
]

# Function to keep track of context
context = {}

def remember_context(user_input):
    context["last_interaction"] = user_input

# Define a simple greeting function
def greeting():
    return "Hello! How can I assist you today?"

# Define a simple farewell function
def farewell():
    return "Goodbye! Have a great day!"

# Chatbot class to handle interaction
class SimpleChatbot:
    def __init__(self, pairs, reflections):
        self.chat = Chat(pairs, reflections)
        self.questions = ["What is your name?", "How can I assist you today?", "Do you need help with anything else?"]
        self.question_index = 0

    def converse(self):
        print(greeting())
        while True:
            if self.question_index < len(self.questions):
                print(f"ChatBot: {self.questions[self.question_index]}")
                self.question_index += 1

            user_input = input("You: ")
            if user_input.lower() in ["bye", "exit", "quit"]:
                print(farewell())
                break

            remember_context(user_input)
            response = self.chat.respond(user_input)
            print(f"ChatBot: {response}")
            print(f"Context: {context}")


bot = SimpleChatbot(pairs, reflections)
bot.converse()
