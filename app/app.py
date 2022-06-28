from flask import Flask
import asyncio
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
def voiceEAPI():
    text = vt.voice_t_module()
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(vr.voice_r_module(text))
    # result = vr.voice_r_module(text)
    # emotionAnalyzers.read_text(text)
    # loop = asyncio.get_event_loop()
    # result = loop.run_until_complete(emotionAnalyzers.analyze(loop=loop))
    return result