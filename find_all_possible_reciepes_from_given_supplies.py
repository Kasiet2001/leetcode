def findAllRecipes(recipes, ingredients, supplies):
    from collections import deque
    res = []
    s = set(supplies)
    dq = deque([(r, ing) for r, ing in zip(recipes, ingredients)])
    p_s = len(s) - 1
    while len(s) > p_s:
        p_s = len(s)
        for _ in range(len(dq)):
            r, ing = dq.popleft()
            if all(i in s for i in ing):
                s.add(r)
                res.append(r)
            else:
                dq.append((r, ing))
    return res
print(findAllRecipes(["bread", 'sandwich'],[["yeast","flour"], ['corn']],["yeast","flour","corn"]))