from datetime import datetime

from flask import Flask, render_template
import random

app = Flask(__name__)

light_levels = []


def add_random_light_level():
    light_levels.append((
        random.randint(0, 1001),
        datetime.now().strftime("%H:%M:%S")
    ))


@app.route("/")
def hello_world():
    add_random_light_level()
    return render_template("greenhouse.html", light_levels=light_levels, time=datetime.now().strftime("%H:%M:%S"))
