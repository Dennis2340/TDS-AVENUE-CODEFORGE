import nltk
from nltk.chat.util import Chat, reflections
from rules import pairs

def chat():
    print("Hi! I am a chatbot created by Geneline-X for your service")
    chat = Chat(pairs=pairs, reflections=reflections)
    chat.converse()
if __name__ == "__main__":
    chat()