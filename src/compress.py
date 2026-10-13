import re
from src.lexical_util import score_overlap

def compress(text: str, query: str, keep_ratio: float = 0.5) -> str:
    sents = [s for s in re.split(r"(?<=[.!?])\s+", text) if s]
    if len(sents) <= 2:
        return text
    k = max(1, int(len(sents) * keep_ratio))
    ranked = sorted(range(len(sents)), key=lambda i: -score_overlap(sents[i], query))[:k]
    return " ".join(sents[i] for i in sorted(ranked))
