def solution(strings, n):
    answer = sorted(strings, key=lambda x: (x[n],x))
    return answer
print(solution(["abce", "abcd", "cdx"], 2))
