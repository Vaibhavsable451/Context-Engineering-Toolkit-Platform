from typing import Callable, List, Optional
from src.tokens import count_tokens

class ConversationMemory:
    """Keeps recent turns verbatim; folds older turns into a rolling summary when over budget."""
    def __init__(self, budget: int = 400, summarizer: Optional[Callable[[str], str]] = None):
        self.budget, self.turns, self.summary = budget, [], ""
        self.summarizer = summarizer or self._naive_summary

    @staticmethod
    def _naive_summary(text: str) -> str:
        return text[:300] + ("..." if len(text) > 300 else "")   # swap for an LLM summarizer

    def add(self, role: str, content: str):
        self.turns.append((role, content))
        while self._size() > self.budget and len(self.turns) > 2:
            role_, old = self.turns.pop(0)
            self.summary = self.summarizer(f"{self.summary}\n{role_}: {old}".strip())

    def _size(self) -> int:
        return count_tokens(self.summary) + sum(count_tokens(c) for _, c in self.turns)

    def render(self) -> str:
        parts = [f"[Summary of earlier conversation] {self.summary}"] if self.summary else []
        parts += [f"{r}: {c}" for r, c in self.turns]
        return "\n".join(parts)
