"""Core StudySprint logic: the deck, the quiz loop, and small helpers."""


def get_cards(data):
    return data["cards"]


def check_answer(card, guess):
    '''Checks to see if the user's response matches the stored correct answer.'''
    return guess.strip().lower() == card["answer"].strip().lower()


def run_quiz(cards, ask=input, show=print):
    score = 0
    results = []
    for card in cards:
        guess = ask(card["question"] + " ")
        if check_answer(card, guess):
            show("Correct!")
            results.append(True)
            score += 1
        else:
            show("Not quite. The answer was: " + card["answer"])
            results.append(False)
    review_missed_cards(cards, results)  
    return score

    
def review_missed_cards(cards,results):
    wrong_ans = []
    for index, correct in enumerate(results):
        if not correct:
            wrong_ans.append(cards[index])
    if wrong_ans == []:
        return wrong_ans
    else:

        print(f"You got {len(wrong_ans)} questions incorrect.")
        print("REVIEW MODE:") 
        run_quiz(wrong_ans)
    return
        
            

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


def count_by_category(cards):
    counts = {}
    for card in cards:
        name = card["category"]
        counts[name] = counts.get(name, 0) + 1
    return counts


def top_card(cards):
    return cards[len(cards) - 1]


def percent_correct(score, total):
    if total == 0:
        return 0
    return round(100 * score / total)