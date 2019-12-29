from flask import Flask, render_template, request
from googleapiclient.discovery import build
import pprint

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


api_key = "AIzaSyBAIubVGkjrcUFeAG-bcYZhuUXCgj_bx00"
cse_id = "015650286644973668229:h8ykdkmq6gu"


@app.route('/', methods=['POST'])
def data_process():
    text = request.form['text']
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=text, cx=cse_id, num=10).execute()
    print(res['url']['items']['snippet'])
    return text

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
