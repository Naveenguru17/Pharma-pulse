from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/detail')
def detail():
    return render_template('detail.html')
@app.route('/mo1ab')
def mo1ab():
    return render_template('mo1ab.html')
@app.route('/mo1ae')
def mo1ae():
    return render_template('mo1ae.html')
@app.route('/no2ba')
def no2ba():
    return render_template('no2ba.html')

@app.route('/no5b')
def no5b():
    return render_template('no5b.html')


@app.route('/search')
def search():
    return render_template('search.html')

if __name__ == "__main__":
    app.run(debug=True)
