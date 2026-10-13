from dataclasses import dataclass
from typing import List, Tuple
from src.packer import pack
from src.reorder import lost_in_middle
from src.compress import compress
from src.tokens import count_tokens

@dataclass
class Budgets:
    total: int = 1500
    system: int = 150
    memory: int = 300
    retrieved: int = 800

def build_context(system: str, memory_text: str, chunks: List[Tuple[str, float]],
                  question: str, b: Budgets = Budgets()) -> dict:
    assert count_tokens(system) <= b.system, "system prompt exceeds its budget - shorten it, never truncate it"
    compressed = [(compress(t, question, 0.7), s) for t, s in chunks]
    picked = pack(compressed, b.retrieved)
    ordered = lost_in_middle([t for t, _ in picked])
    evidence = "\n".join(f"<doc {i+1}>{t}</doc {i+1}>" for i, t in enumerate(ordered))
    prompt = (f"{system}\n\n### Conversation\n{memory_text}\n\n### Evidence\n{evidence}\n\n"
              f"### Question\n{question}")
    return {"prompt": prompt, "tokens": count_tokens(prompt), "docs_used": len(picked), "docs_offered": len(chunks)}
