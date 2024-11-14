def maximumBeauty(items, queries):
    items.sort()
    ans = [0] * len(queries)
    p = ind = 0
    q = ((x, i) for i, x in enumerate(queries))
    for x, i in sorted(q):
        while ind < len(items) and items[ind][0] <= x:
            p = max(p, items[ind][1])
            ind += 1
        ans[i] = p
    return ans
print(maximumBeauty([[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]], [885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]))