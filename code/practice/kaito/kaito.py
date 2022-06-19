import speech_recognition as sr
import subprocess


def Getspeaking_value():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("=== 何か、話しかけてください ===")
        audio = r.listen(source)
        print("[o] ===> オーディオGET")

    try:
        print("=== CMU Sphinx音声解析中 ===")
        text = r.recognize_sphinx(audio)
        if (text in ['come on it', 'oh my', 'come on that', 'oh my']):  # ここで英語->日本語変換判断
            print("You said : " + "とまれ")
    except:
        print("error")
        pass
    try:
        print("=== Google Speech Recognition音声解析中 ===")
        text = r.recognize_google(audio, language="ja-JP")
        print("You said : " + text)
    except:
        print("error")
        pass


if __name__ == "__main__":
    Getspeaking_value()