import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        name = request.form["name"]
        bio = request.form["name"]
        line_type = request.form["line_type"]

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(name, bio, line_type),
            temperature=0.6,
            max_tokens=1000
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(name, bio, line_type):
    return f"""
    
Suggest three pick-up lines based on name and or a short bio.
If at the start I say name base the pickup line on the name.
If I say bio then base the pickup line on the bio. 
Here are some examples

Type: Name
Name: Mady
Bio: Blonde, 24, love coffee and partying
Pick-up line: You know if you remove the d from your name it becomes May. So the question is, do you want the d?

Type: Name
Name: Sarah
Bio: 24, love reading, I will ruin your life.
Pick-up line: I was trying to come up with a good pick up line but I figured I could just Sarah-made you tonight


Type: Bio
Name: Francesca
Bio: 26, tall, love chess
Pick-up line: I've been sat here trying to come up with a chess related pick up line to use...But I've just realised
that's pointless. Because you probably know all the openings! 

Type: Bio
Name: Jessica
Bio: daddy issues 
Pick-up line: Let ,e turn your daddy issues into baby daddy isssues


Type: {line_type.capitalize()}
Name: {name.capitalize()}
Bio: {bio}
Pick-up line:"""
