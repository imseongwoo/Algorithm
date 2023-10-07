def solution(answers):
    answer = []
    result = []

    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    length = len(answers)
    tmp = 0

    cnt = 0
    cnt2 = 0
    cnt3 = 0
    while tmp != length:
        for a in answers:
            compare1 = one.pop(0)
            compare2 = two.pop(0)
            compare3 = three.pop(0)

            if compare1 == a:
                cnt += 1

            if compare2 == a:
                cnt2 += 1

            if compare3 == a:
                cnt3 += 1

            one.append(compare1)
            two.append(compare2)
            three.append(compare3)

            tmp += 1

    answer.append(cnt)
    answer.append(cnt2)
    answer.append(cnt3)

    maxvalue = max(answer)

    answer = enumerate(answer)
    for idx,value in answer:
        if value == maxvalue:
            result.append(idx+1)

    return result



print(solution([1,3,2,4,2]))


def solution(answers):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == student1[idx%len(student1)]:
            score[0] += 1
        if answer == student2[idx%len(student2)]:
            score[1] += 1
        if answer == student3[idx%len(student3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
