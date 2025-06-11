from flask import Flask, render_template, request
from functions import fetch_events

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    city = request.form['city']
    events = fetch_events(city)  
    return render_template('result.html', events=events, city=city)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
