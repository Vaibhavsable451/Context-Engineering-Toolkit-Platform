from src.builder import build_context, Budgets
from src.memory import ConversationMemory

SYSTEM = "You are a precise assistant. Use only the evidence. If it is insufficient, say so."
mem = ConversationMemory(budget=120)
for i in range(6):
    mem.add("user", f"Question number {i}: tell me about policy topic {i} in great detail please.")
    mem.add("assistant", f"Answer {i}: here is a long detailed explanation about policy topic {i}. " * 3)

chunks = [
    ("Meals are reimbursed up to 60 USD per day. Flights over 500 USD need approval. Receipts are due in 30 days.", 0.92),
    ("Meals are reimbursed up to 60 USD per day. Flights over 500 USD need approval. Receipts are due in 30 days.", 0.90),
    ("Parental leave is 16 weeks fully paid. Vacation is 20 days.", 0.30),
    ("The office cafeteria opens at 8am. Coffee is free. Lunch costs 6 USD.", 0.40),
]
out = build_context(SYSTEM, mem.render(), chunks, "What is the daily meal reimbursement limit?", Budgets())
print(out["prompt"]); print(f"\n--- tokens={out['tokens']} docs_used={out['docs_used']}/{out['docs_offered']} (duplicates removed) ---")
