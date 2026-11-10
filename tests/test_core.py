"""Example tests for StudySprint. Two small tests to copy from in Lesson 12."""

import unittest

from features import core


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

    def test_review_missed_mixed_results(self):
        cards = [
            {"id": 1, "question": "France?"},
            {"id": 2, "question": "Italy?"},
            {"id": 3, "question": "Japan?"}
        ]

        results = [True, False, True]

        missed = core.review_missed(cards, results)

        self.assertEqual(missed, [cards[1]])

    def test_review_missed_nothing_missed(self):
        cards = [
            {"id": 1, "question": "France?"},
            {"id": 2, "question": "Italy?"}
        ]

        results = [True, True]

        missed = core.review_missed(cards, results)

        self.assertEqual(missed, [])



if __name__ == "__main__":
    unittest.main()
