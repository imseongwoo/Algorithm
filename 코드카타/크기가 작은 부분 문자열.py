def solution(t, p):
    answer = 0
    num = []
    for i in range(len(t) - len(p) + 1):
        num.append(t[i:i+len(p)])

    for a in num:
        if int(a) <= int(p):
            answer+=1
    print(num)
    return answer


solution("500220839878", "7")
