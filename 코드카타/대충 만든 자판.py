from collections import deque

def solution(keymap, targets):
    answer = []
    targets = deque(targets)

    while targets:
        target = targets.popleft()
        count = 0
        possible = True
        for a in target:
            minval = 999999999
            flag = False
            for key in keymap:
                if a in key:
                    minval = min(minval, key.index(a))
                    flag = True

            if not flag:
                count = -1
                possible = False
                break
            count += (minval + 1)
        if not possible:
            answer.append(-1)
        else:
            answer.append(count)

    return answer


from collections import deque


def solution(keymap, targets):
    answer = []
    targets = deque(targets)

    while targets:
        target = targets.popleft()
        count = 0
        possible = True

        for char in target:
            min_presses = float('inf')
            found = False

            for i, key in enumerate(keymap):
                presses = 1
                for k in key:
                    if k == char:
                        min_presses = min(min_presses, presses)
                        found = True
                    presses += 1

            if not found:
                count = -1
                possible = False
                break
            count += min_presses

        if not possible:
            answer.append(-1)
        else:
            answer.append(count)

    return answer

solution(["ABACD", "BCEFD"], ["ABCD","AABB"])