from dataclasses import dataclass

@dataclass
class Sentiment:
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"