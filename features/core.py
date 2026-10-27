"""Core StudySprint logic: the deck, the quiz loop, and small helpers."""


def get_cards(data):
    return data["cards"]


def check_answer(card, guess):
    """Check to see if user's answer matches the stored question answer."""
    return guess.strip().lower() == card["answer"].strip().lower()


def run_quiz(cards, ask=input, show=print):
    results = []
    for card in cards:
        guess = ask(card["question"] + " ")
        if check_answer(card, guess):
            show("Correct!")
            results.append(True)
        else:
            show("Not quite. The answer was: " + card["answer"])
            results.append(False)
    return results

def score(results):
    score = 0
    for result in results:
        if result:
            score += 1
    return score


def add_card(data, question, answer, category="general"):
    new_id = max((c["id"] for c in data["cards"]), default=0) + 1
    card = {"id": new_id, "question": question, "answer": answer, "category": category}
    data["cards"].append(card)
    return card


def list_cards(cards, show=print):
    for card in cards:
        show(str(card["id"]) + ". " + card["question"])


def cards_by_category(cards, category):
    return [c for c in cards if c["category"] == category]


def top_card(cards):
    return cards[len(cards) - 1]


def percent_correct(score, total):
    if total == 0:
        return 0
    return round(100 * score / total)

def best_streak(results):
    # assume results is a list of booleans

    start_streak = False
    count = 0
    max_count = 0
    for result in results:
        if result:
            count += 1
            if not start_streak:
                start_streak = True
        if not result and start_streak:
            max_count = max(max_count, count)
            count = 0

    return max_count