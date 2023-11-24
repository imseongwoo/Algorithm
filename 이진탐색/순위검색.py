from itertools import combinations
from collections import defaultdict
from bisect import bisect_left as left_bound


def solution(info, query):
    answer = []
    people = defaultdict(list)

    for i in info:
        person = i.split()
        score = int(person.pop())
        people[''.join(person)].append(score)

        for j in range(4):
            candi = list(combinations(person, j))
            for c in candi:
                people[''.join(c)].append(score)

    for i in people: people[i].sort()

    for i in query:
        key = i.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-', '')
        answer.append(len(people[key]) - left_bound(people[key], score))

    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"]))


# 틀림
# from itertools import combinations
# from collections import defaultdict
# from bisect import bisect_left
#
# def solution(info, query):
#     answer = []
#     people = defaultdict(list)
#
#     for a in info:
#         answer = a.split(' ')
#         score = answer[-1]
#         answer.pop()
#         dictkeylist = answer[:-1]
#         dictkey = ''.join(dictkeylist)
#         people[dictkey].append(score)
#
#         for j in range(4):
#             case = list(combinations(dictkeylist, j))
#             for c in case:
#                 people[''.join(c)].append(score)
#
#     for i in people:
#         people[i].sort()
#
#     for i in query:
#         key = i.split(' ')
#         queryscore = key[-1]
#         key.pop()
#         key = ''.join(key)
#         key = key.replace('and','').replace(' ','').replace('-','')
#         answer.append(len(people[key])-bisect_left(people[key],queryscore))
#     return answer
