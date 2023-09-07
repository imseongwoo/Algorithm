def solution(s):
    word = s.split(' ')
    res = []
    for a in word:
        length = len(a)
        a = list(a)
        for b in range(length):
            if b % 2 == 0:
                a[b] = a[b].upper()
            else:
                a[b] = a[b].lower()
        res.append(''.join(a))

    return " ".join(res)

print(solution("try hello world"))

# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하라
