from flask import Flask
import random

app = Flask(__name__)

jokes = [
    "Whats the object-oriented way to become wealthy? Inheritance",
    "!false - It's funny 'cause it's true.",
    "Why did the functions stop calling each other? Because they had constant arguments."
    "Git Status Test"
]


@app.get("/")
def tell_a_joke():
    joke = random.choice(jokes)
    return f"<p>{joke}</p>"
