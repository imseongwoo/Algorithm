def solution(number, k):
    answer = []

    for a in number:
        while k > 0 and answer and answer[-1] < a:
            answer.pop()
            k -= 1
        answer.append(a)

    return ''.join(answer[:len(number) - k])


print(solution("4177252841", 4))

# 51111-> 처음에 5들어가고 이후부터는 전부 5보다 작으므로 k는 그대로인데 리스트에 전부 들어가 있음 -> 뒤에서 k만큼 뺀 곳 까지만 정답으로
