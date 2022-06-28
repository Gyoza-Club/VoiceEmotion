# 音声認識
from transformers import pipeline, AutoModelForSequenceClassification, BertJapaneseTokenizer
# import codecs
import asyncio

class SentimentAnalysis:
    def __init__(self):
        """
        コンストラクタ
        """
        model = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment')
        tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
        self.nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
        self.document = None

    async def analyze(self, text=None):
        '''
        感情分析
        '''
        result = self.nlp(self.document if text is None else text)
        return result

    def read_text(self, text):
        '''
        テキストの読み込み

        Parameters:
        --------
            text : str   TF-IDFしたい文書
        '''
        # 形態素解析を用いて名詞のリストを作成
        self.document = text
        return

async def voice_r_module(text):
    em = SentimentAnalysis()
    em.read_text(text)
    result = await em.analyze()
    return result