# the function does not call the function, instead a reference to that
# function is created
def shout(text):
    return text.upper()

print(shout("hello"))

yell = shout

print(yell("hello world"))