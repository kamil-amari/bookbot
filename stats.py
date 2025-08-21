from collections import defaultdict


def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> list[tuple]:
    count = defaultdict(int)
    for c in text.lower():
        count[c] += 1
    return sorted(count.items(), key=lambda x: x[1], reverse=True)