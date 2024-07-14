def minimumCost(m, n, horizontalCut, verticalCut):
    horizontalCut.sort(reverse=True)
    verticalCut.sort(reverse=True)

    horPiece = 1
    verPiece = 1
    ans = 0

    h_idx = 0
    v_idx = 0

    while h_idx < len(horizontalCut) and v_idx < len(verticalCut):
        if horizontalCut[h_idx] >= verticalCut[v_idx]:
            ans += horizontalCut[h_idx] * verPiece
            horPiece += 1
            h_idx += 1
        else:
            ans += verticalCut[v_idx] * horPiece
            verPiece += 1
            v_idx += 1

    while h_idx < len(horizontalCut):
        ans += horizontalCut[h_idx] * verPiece
        horPiece += 1
        h_idx += 1

    while v_idx < len(verticalCut):
        ans += verticalCut[v_idx] * horPiece
        verPiece += 1
        v_idx += 1

    return ans

print(minimumCost(3, 2, [1, 3], [5]))  # Output should be 13
