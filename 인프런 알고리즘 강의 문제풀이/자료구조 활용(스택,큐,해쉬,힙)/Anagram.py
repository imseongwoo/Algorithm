arr = list(input())
arr2 = list(input())
count = 0
for a in arr:
    if a in arr2:
        arr2.remove(a)
    else:
        print('NO')
        break
else:
    print('YES')

# 답
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x,0) + 1
for x in b:
    str2[x] = str2.get(x,0) + 1     # x라는 키 값이 없으면 0 반환
for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print('NO')
        break
else:
    print('YES')

# counter 모듈 사용
from collections import Counter
word1 = input()
word2 = input()

res = Counter(word1) - Counter(word2)
if len(res) == 0:
    print('YES')
else:
    print('NO')

#개선된 코드
import sys
#sys.stdin=open("in1.txt", "r")
a=input()
b=input()
sH=dict()
for x in a:
    sH[x]=sH.get(x, 0)+1
for x in b:
    sH[x]=sH.get(x, 0)-1

for x in a:
    if(sH.get(x)>0):
        print("NO")
        break;
else:
    print("YES")

# 리스트 해쉬
import sys

a=input()
b=input()
str1=[0]*52
str2=[0]*52
for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1
    else:
        str1[ord(x)-71]+=1
for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
    else:
        str2[ord(x)-71]+=1
for i in range(52):
    if str1[i]!=str2[i]:
        print("NO")
        break
else:
    print("YES")












