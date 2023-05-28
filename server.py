from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('output.txt', 'r') as f:
        entries = json.load(f)

    return render_template('documentation.html', entries=entries)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
