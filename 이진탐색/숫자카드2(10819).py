import bisect
import sys
input = sys.stdin.readline

n = int(input())
card_num = list(map(int,input().split()))
m = int(input())
target_list = list(map(int,input().split()))

card_num.sort()

for a in target_list:
    left = bisect.bisect_left(card_num, a)      # 찾아야 하는 값의 왼쪽 인덱스 반환
    right = bisect.bisect_right(card_num, a)    # 찾아야 하는 값의 오른쪽 인덱스 반환
    print(right - left, end=' ')                #  찾아야 하는 값이 없으면 0 이 반환됨


# 내장 모듈 Couner 를 이용한 풀이

from collections import Counter

n = int(input())
card_num = list(map(int,input().split()))
m = int(input())
target_list = list(map(int,input().split()))
res = []
card_num = Counter(card_num)
print(card_num)
for a in target_list:
    res.append(card_num[a])

for i in res:
    print(i,end=' ')