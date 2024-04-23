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
