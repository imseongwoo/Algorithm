

def solution(s, skip, index):
    answer = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    for char in s:
        start = alphabet.index(char)
        count = 0
        while count < index:
            start = (start + 1) % 26
            if alphabet[start] not in skip:
                count += 1

        answer += alphabet[start]

    return answer


print(solution("ab", "c", 1))