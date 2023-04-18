def maxProfitAssignment(difficulty, profit, worker):
    jobs = sorted(zip(difficulty, profit))
    res = ind = best = 0
    for i in sorted(worker):
        while ind < len(jobs) and i >= jobs[ind][0]:
            best = max(jobs[ind][1], best)
            ind += 1
        res += best
    return res
print(maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]))