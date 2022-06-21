# from flask import *
# import voiceRecognition as vr
# import voiceTextualization as vt
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello():
#     return "Hello!"
#
# # 音声認識用API
# @app.route('/vr')
# def voiceRecognition():
#     return vr.voice_r_module()
#
# # 音声テキスト化用API
# @app.route('/vt')
# def voiceTextualization():
#     return vt.voice_t_module()

from flask import Flask, jsonify, request
import json
import urllib.request
import xmltodict

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/", methods=['GET'])
def index():
    # パラメーター取得
    keyword = request.args.get('keyword')
    # API通信
    req = "https://news.google.com/rss/search?q=" + urllib.parse.quote_plus(keyword, encoding='utf-8') + "&hl=ja&gl=JP&ceid=JP:ja"
    # 結果取得
    with urllib.request.urlopen(req) as res:
        body = res.read()
    # XML → 辞書に変換
    dict = xmltodict.parse(body)
    # 辞書 → JSONに変換
    data = json.dumps(dict, indent=4, ensure_ascii=False)
    # 結果返却
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

