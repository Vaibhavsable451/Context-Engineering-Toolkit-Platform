# 07 - Context Engineering Toolkit

Control **what goes into the context window**, since most "hallucinations" are really context failures.

| Module | Technique |
|---|---|
| `tokens.py` | Token counting (tiktoken, with a char/4 fallback) |
| `packer.py` | Budgeted context packing, de-duplication, relevance ordering |
| `reorder.py` | "Lost in the middle" reordering (best chunks at start and end) |
| `memory.py` | Conversation memory: sliding window + rolling summary when over budget |
| `compress.py` | Extractive sentence compression to the query |
| `builder.py` | Assembles system / memory / retrieved / question sections with explicit budgets |

```bash
pip install -r requirements.txt
python -m src.demo
python -m unittest discover tests
```
Rules of thumb it encodes: put instructions first, evidence at the edges, question last; budget every section; compress before you truncate; never silently drop the system prompt.
