
from flask import Flask, render_template
import random

app = Flask(__name))

@app("/")
def index():

    toss = random.randint(0,2)
    if toss:
        print("Go out!")
    else:
        print("Stay in!")
