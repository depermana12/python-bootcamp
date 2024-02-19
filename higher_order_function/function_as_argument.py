# funtions are like objects in python, they can be passed as arguments to other functions

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greetings = func("Hello, i am created by a function passed as argument")
    print(greetings)

greet(shout)
greet(whisper)