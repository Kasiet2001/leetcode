from collections import defaultdict
def queryResults(limit, queries):
    colors_of_nums = dict()
    num_of_colors = defaultdict(int)
    result = []
    for x, y in queries:
        if x in colors_of_nums:
            if colors_of_nums[x] in num_of_colors:
                num_of_colors[colors_of_nums[x]] -= 1
            if colors_of_nums[x] in num_of_colors:
                if num_of_colors[colors_of_nums[x]] < 1:
                    num_of_colors.pop(colors_of_nums[x])
        num_of_colors[y] += 1
        colors_of_nums[x] = y
        result.append(len(num_of_colors))
    return result
print(queryResults(4, [[0,1],[1,2],[2,2],[3,4],[4,5]]))

