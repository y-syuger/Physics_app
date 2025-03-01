from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# Jsonから問題を取得
def load_questions():
    with open('data/questions.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)
        return questions

@app.route('/')
def index():
    questions_data = load_questions()
    return render_template('index.html', questions=questions_data)

if __name__ == '__main__':
    app.run(debug=True)