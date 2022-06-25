from flask import Flask
import voiceRecognition as vr
import voiceTextualization as vt

app = Flask(__name__)

@app.route("/")
def index():
    return "index page"

@app.route("/vr")
def voiceRecognition():
    return vr.voice_r_module()

@app.route("/vt")
def voiceTextualization():
    return vt.voice_t_module()

