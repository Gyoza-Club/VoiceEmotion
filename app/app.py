from flask import Flask, jsonify
import voiceRecognition as vr
import voiceTextualization as vt

app = Flask(__name__)

@app.route("/")
def index():
    return "index page"

@app.route("/vr")
def voiceRecognition():
    # emotionAnalyzers = vr.SentimentAnalysis()
    # emotionAnalyzers.read_text("こんにちは！今日は楽しい日になりそうですね!")
    # result = emotionAnalyzers.analyze()
    return "result"

@app.route("/vt")
def voiceTextualization():
    return vt.voice_t_module()

@app.route("/test")
def voicert():
    text = vt.voice_t_module()
    return jsonify(vr.voice_r_module(text))