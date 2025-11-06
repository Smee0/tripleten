print("Hello World!")
print("Learning about commits today!")
print("You can do the same with 10 lines of code as you can with 100 lines of codes - Mr. G")

import random

greetings = [
    "Hello, Git!",
    "Greetings, developer!",
    "Welcome to branching!",
    "Hi there, coding friend!",
    "Happy coding!"
]

def get_random_greeting():
    return random.choice(greetings)

print(get_random_greeting())
print("Learning about branches today!")