def bigGreeting(func):
    func()

@bigGreeting
def greetings():
    print('Hello World')

greetings()
