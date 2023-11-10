def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            sum = numbers[i]+numbers[j]
            if sum in answer:
                continue
            else:
                answer.append(sum)
    answer = sorted(answer)
    return answer



print(solution([5,0,2,7]))