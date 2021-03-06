from flask import Flask, render_template, request
from googleapiclient.discovery import build
import pprint

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


api_key = "Enter your API key..."
cse_id = "Custom Search Engine ID.."


@app.route('/', methods=['POST'])
def data_process():
    text = request.form['text']
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=text, cx=cse_id, num=10).execute()
    print(res)
    return text

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
