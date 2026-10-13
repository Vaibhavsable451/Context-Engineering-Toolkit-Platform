from typing import List, Tuple
from src.tokens import count_tokens

def pack(chunks: List[Tuple[str, float]], budget: int) -> List[Tuple[str, float]]:
    """chunks = [(text, relevance_score)]. Greedy by score, skip duplicates, stop at token budget."""
    seen, picked, used = set(), [], 0
    for text, score in sorted(chunks, key=lambda x: -x[1]):
        key = " ".join(text.lower().split())
        if key in seen:
            continue
        n = count_tokens(text)
        if used + n > budget:
            continue
        seen.add(key); picked.append((text, score)); used += n
    return picked
