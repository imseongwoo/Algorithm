def solution(s):
    cnt = 0
    transcount = 0

    while s != '1':
        transcount += 1
        num = s.count('1')
        cnt += len(s) - num
        print(bin(num))
        s = bin(num)[2:]

    return [transcount, cnt]


result = solution("0111010")
print(result)
