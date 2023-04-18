def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    sum_rec = (ax1 - ax2) * (ay1 - ay2) + ((bx1 - bx2) * (by1 - by2))
    return sum_rec - max(min(ax2, bx2) - max(ax1, bx1), 0) * max(min(ay2, by2) - max(ay1, by1), 0)
print(computeArea(-2, -2, 2, 2, -2, -2, 2, 2))