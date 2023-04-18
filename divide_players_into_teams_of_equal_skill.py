def dividePlayers(skill):
    skill.sort()
    ind = -2
    l = len(skill)
    s = [skill[0] + skill[-1]]
    ans = skill[0] * skill[-1]
    for i in range(1, l//2):
        if skill[i] + skill[ind] not in s:
            return -1
        else:
            ans += skill[i] * skill[ind]
            ind -= 1
    return ans
print(dividePlayers([3,2,5,1,3,4]))