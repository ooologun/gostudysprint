"""Example tests for StudySprint. Two small tests to copy from in Lesson 12."""

import unittest

from features import core, reports


class TestCore(unittest.TestCase):
    def test_check_answer_is_case_insensitive(self):
        card = {"id": 1, "question": "Capital of France?", "answer": "Paris", "category": "geo"}
        self.assertTrue(core.check_answer(card, "paris"))
        self.assertFalse(core.check_answer(card, "London"))

    def test_add_card_gives_a_new_id(self):
        data = {"cards": [{"id": 1, "question": "q", "answer": "a", "category": "general"}]}
        card = core.add_card(data, "New question?", "yes")
        self.assertEqual(card["id"], 2)
        self.assertEqual(len(data["cards"]), 2)

    def test_category_breakdown(self):
        cards = [
            {"id": 1, "question": "q", "answer": "a", "category": "syntax"},
            {"id": 2, "question": "q", "answer": "a", "category": "types"},
            {"id": 3, "question": "q", "answer": "while", "category": "syntax"},
            {"id": 4, "question": "q", "answer": "a", "category": "syntax"},
            {"id": 5, "question": "q", "answer": "a", "category": "lists"},
            {"id": 6, "question": "q", "answer": "a", "category": "syntax"},
            {"id": 7, "question": "q", "answer": "a", "category": "types"},
            {"id": 8, "question": "q", "answer": "a", "category": "io"},
            {"id": 9, "question": "q", "answer": "a", "category": "general"},
            {"id": 9, "question": "q", "answer": "a", "category": "general"},
        ];
        categories = {"syntax": 4, "types": 2, "lists": 1, "io": 1, "general": 2}

        self.assertEqual(reports.category_report(cards), categories)
        


if __name__ == "__main__":
    unittest.main()
