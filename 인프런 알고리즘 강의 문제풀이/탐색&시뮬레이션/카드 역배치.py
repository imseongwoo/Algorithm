# 내가 푼 방법
card = []
card.append(0)
for i in range(20):
    card.append(i+1)

for _ in range(10):
    a,b = map(int,input().split())
    le = (b-a+1)//2
    for i in range(le):
        card[a],card[b] = card[b],card[a]
        a += 1
        b -= 1
card.remove(0)
print(card,end=' ')

# 답

a = list(range(21)) # append 할 필요가 없었다
for _ in range(10):
    s,e = map(int,input().split())
    for i in range((e-s+1)//2):
        a[s+i],a[e-i] = a[e-i],a[s+i]
a.pop(0)    # 0번 인덱스를 pop해라.
for x in a:
    print(x,end=' ')