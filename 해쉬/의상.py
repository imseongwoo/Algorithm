# 서로 다른 조합의 수 구하기

def solution(clothes):
    answer = 1
    dict = {}
    for a in clothes:
        dict[a[1]] = dict.get(a[1],0)+1

    for a in dict:
        answer *= dict[a]+1

    return answer-1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])