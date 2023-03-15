from transformers import pipeline
from sentiment_enum import Sentiment
from tqdm import tqdm

MODEL_DIR = 'cardiffnlp/twitter-roberta-base-sentiment-latest'

class SentimentAnalyzer:

    def __init__(self):
        self._analyze_pipeline = pipeline(
            task='sentiment-analysis',
            model=MODEL_DIR,
            tokenizer=MODEL_DIR,
        )

    def analyze(self, text: str):
        analysis = self._analyze_pipeline(text)[0]
        if analysis["label"] == 'positive':
            return (1, analysis["score"])
        elif analysis["label"] == 'negative':
            return (-1, analysis["score"])
        else:
            return (0, analysis["score"])

    def batch_analysis(self, posts: list) -> list:
        sentiment = []
        for i, post in tqdm(enumerate(posts)):
            try:
                sentiment.append(self.analyze(post))
            except:
                print (f"Sentiment Analysis Failed on post #{i}")
                sentiment.append((0, float(0.0)))
        return sentiment

    def calculate_accuracy(self, pred_labels: list, correct_labels: list, confidence_min=0.0) -> float:
        if len(pred_labels) != len(correct_labels):
            return -1
        correct_total = 0
        total = 0
        for i, prediction in enumerate(pred_labels):
            if prediction[1] < confidence_min:
                continue
            total += 1
            correct_total += \
                (prediction[0] == Sentiment.POSITIVE and correct_labels[i] == 1) + \
                (prediction[0] == Sentiment.NEUTRAL and correct_labels[i] == 0) + \
                (prediction[0] == Sentiment.NEGATIVE and correct_labels[i] == -1)
        return (correct_total/total, total)
    
    def calculate_adjusted_accuracy(self, pred_labels, correct_labels, confidence_min=0):
        num_correct = 0
        for idx, pair in enumerate(pred_labels): 
            if pair[0] != correct_labels[idx]:
                num_correct += (0.5-pair[1])
            else:
                num_correct += 1 + (pair[1] - 0.5)
        return num_correct / len(correct_labels)