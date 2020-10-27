n = int(input())
count = 0
def check(words):
    stan = words[0]
    global count
    chklist = []
    chklist.append(words[0])
    for i in range(1,len(words)):
        if stan != words[i]:
            if words[i] not in chklist:
                stan = words[i]
                chklist.append(words[i])
            else:
                return False
        else:
            continue
    count += 1

for _ in range(n):
    word = input()
    check(word)
print(count)