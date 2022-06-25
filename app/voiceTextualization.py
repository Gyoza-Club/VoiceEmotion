# 音声テキスト化
import speech_recognition as sr

def voice_t_module():
    voicePath = "./voiceData/voice1.wav"
    r = sr.Recognizer()
    with sr.AudioFile(voicePath) as source:
        audio = r.record(source)
    text = r.recognize_google(audio, language='ja-JP')
    return text