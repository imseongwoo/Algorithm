from collections import deque

def check(word,temp):
    temp = list(temp)
    templen = len(temp)
    length = len(word)
    count = 0

    for i in range(length):
        if word[i] in temp:
            temp.remove(word[i])
            count += 1

    if templen-count == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    count = 0
    queue = deque()
    queue.append((begin,0))
    ch = [0]*len(words)
    while queue:
        temp = queue.popleft()
        if temp[0] == target:
            return temp[1]

        for i in range(len(words)):
            if ch[i] != 1:
                if check(words[i],temp[0]):
                    queue.append((words[i],temp[1]+1))
                    ch[i] = 1
    return count

print(solution("aab", "aba", ["abb", "aba"]))