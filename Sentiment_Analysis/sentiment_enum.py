from dataclasses import dataclass

@dataclass
class Sentiment:
    POSITIVE = 1
    NEUTRAL = 0
    NEGATIVE = -1