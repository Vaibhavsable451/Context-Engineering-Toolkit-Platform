import unittest
from src.packer import pack
from src.reorder import lost_in_middle
from src.memory import ConversationMemory
from src.tokens import count_tokens

class T(unittest.TestCase):
    def test_pack_dedupe_budget(self):
        r = pack([("alpha beta", 0.9), ("alpha beta", 0.8), ("gamma " * 200, 0.7)], budget=50)
        self.assertEqual(len(r), 1)
    def test_reorder(self):
        self.assertEqual(lost_in_middle([1, 2, 3, 4, 5]), [1, 3, 5, 4, 2])
    def test_memory_budget(self):
        m = ConversationMemory(budget=60)
        for i in range(10): m.add("user", "word " * 30)
        self.assertTrue(m.summary)
        self.assertLessEqual(len(m.turns), 3)

if __name__ == "__main__":
    unittest.main()
