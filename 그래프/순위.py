from collections import defaultdict

def solution(n, results):
    answer = 0
    wins = defaultdict(set)
    lose = defaultdict(set)

    for winner, loser in results:
        wins[winner].add(loser)
        lose[loser].add(winner)
    print(wins, lose)

    for i in range(1, n+1):
        for winner in wins[i]:
            lose[winner].update(lose[i])
        for loser in lose[i]:
            wins[loser].update(wins[i])

    for a in wins:
        if len(wins[a]) + len(lose[a]) == n-1:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))