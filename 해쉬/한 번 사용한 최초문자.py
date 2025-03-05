def solution(word):
    diction = {}
    for alp in word:
        diction[alp] = diction.get(alp,0)+1
    for a in diction:
        if diction[a] == 1:
            return list(word).index(a)+1
    return -1

print(solution("statitsics"))
print(solution("aabb"))
print(solution("abcdeabcdfg"))