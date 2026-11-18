"""Reporting helpers for StudySprint.

Heads up: this module is half-built on purpose. `deck_summary` works, but
`category_report` is still a stub with a clear seam to finish (see the tickets).
"""

def deck_summary(data):
    return data["deck_name"] + ": " + str(len(data["cards"])) + " cards"


def category_report(cards):
    report = {}
    for card in cards:
        name = card["category"]
        report[name] = report.get(name, 0) + 1
    return report
