from collections import deque
def deckRevealedIncreasing(deck):
    deck.sort()
    ans = [0] * len(deck)
    idxs = deque(range(len(deck)))
    for card in deck:
        idx = idxs.popleft()
        ans[idx] = card
        if idxs:
            idxs.append(idxs.popleft())
    return ans