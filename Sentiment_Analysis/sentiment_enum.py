from dataclasses import dataclass

@dataclass
class Sentiment:
    POSITIVE = 1
    NEUTRAL = 0
    NEGATIVE = -1

LABEL_TO_NUM = {'positive': 1, 'negative': -1, 'neutral': 0}
