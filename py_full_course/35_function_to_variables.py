from os import terminal_size


def hello():
    print("Hello")

greeting = hello # hello ham greeting ham bitta manzilga ko'rsatadi.

print(hello) # masalan, <function hello at 0x7f76a196c040>
print(greeting) # <function hello at 0x7f76a196c040>

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func): # higher order function
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

def divisor(x): # this is also higher order function
    def dividend(y):
        return y / x
    return dividend

divide = divisor(3)
print(divide(9))

