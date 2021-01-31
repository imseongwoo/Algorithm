n = int(input())
note = []
delnote = []

for _ in range(n):
    note.append(input())
for _ in range(n-1):
    delnote.append(input())
for a in delnote:
    if a in note:
        note.remove(a)

for b in note:
    print(b)

# 답
n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1):
    word = input()
    p[word] = 0

for key,value in p.items():
    if value == 1:
        print(key)
        break