from collections import defaultdict

def dfs(arr,path,visit):
    if path:
        to = path[-1]
        if arr[to]:
            path.append(arr[to].pop(0))
        else:
            visit.append(path.pop())
        print(path)
        dfs(arr,path,visit)

    return visit[::-1]

def solution(tickets):
    answer = []
    arr = defaultdict(list)

    for a,b in tickets:
        arr[a].append(b)

    for key in arr.keys():
        arr[key].sort()
    print(arr)
    return dfs(arr,["ICN"],[])


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))