def check(word):
    for idx, a in enumerate(word):
        if a != 'A':
            return idx


def solution(name):
    answer = 0
    for idx, a in enumerate(name):
        if a == 'A':
            continue

        cnt = min(ord(a) - ord('A'), ord('Z') - ord(a) + 1)
        answer += cnt

        if name[idx + 1:] == 'A' * (len(name[idx + 1:])):
            return answer
        else:
            charidx = check(name[idx + 1:])
            if idx == 0:
                charidx = charidx + 1
            else:
                charidx = charidx + idx + 1
            print(charidx)
            minmove = min(charidx - idx, len(name) - charidx)
            answer += minmove

    return answer


print(solution("JEROEN"))

# 틀렸어.. ㅠㅠ

def solution(name):
    answer = 0
    size = len(name)
    min_move = size - 1

    for idx, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next_idx = idx + 1
        while next_idx < size and name[next_idx] == 'A': next_idx += 1

        min_move = min([min_move, 2 * idx + size - next_idx, idx + 2 * (size - next_idx)])

    answer += min_move
    return answer
# 이게 올바른 코드


