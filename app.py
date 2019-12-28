from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def data_process():
    text = request.form['text']
    print(text)
    return text

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
