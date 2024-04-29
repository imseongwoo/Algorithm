def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for idx, a in enumerate(answers):
        if a == three[idx % len(three)]:
            score[2] += 1
        if a == two[idx % len(two)]:
            score[1] += 1
        if a == one[idx % len(one)]:
            score[0] += 1

    max_value = max(score)
    for idx, a in enumerate(score):
        if a == max_value:
            answer.append(idx + 1)

    return answer

print(solution([1, 3, 2, 4, 2]))
