import re
def _t(s): return set(re.findall(r"[a-z0-9]+", s.lower()))
def score_overlap(a: str, b: str) -> float:
    A, B = _t(a), _t(b)
    return len(A & B) / (len(B) or 1)
