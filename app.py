from flask import Flask, render_template
import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask/<q>')
def ask(q):
    return render_template('index.html', question=q)

if __name__ == '__main__':
    app.run(debug=True)