import math
from collections import defaultdict
map = defaultdict(list)

# 올림
print(math.ceil(3.14))
print(math.ceil(-3.14))

# 내림
print(math.floor(12.34))

# 소수점 버림
math.trunc(12.34) # 12

num = 12345.6789

print("기존 값 : ", num)
print("1 의 자리에서 반올림 : ", round(num, -1))
print("10 의 자리에서 반올림 : ", round(num, -2))
print("100 의 자리에서 반올림 : ", round(num, -3))
print("1000 의 자리에서 반올림 : ", round(num, -4))
print("소수 첫번째 자리에서 반올림 : ", round(num))
print("소수 두번째 자리에서 반올림 : ", round(num, 1))
print("소수 세번째 자리에서 반올림 : ", round(num, 2))
print("소수 네번째 자리에서 반올림 : ", round(num, 3))

print(math.trunc(num*100)/100)


#딕셔너리
map = dict()
map["value"] = 3
if 3 in map.values():
    print(map.keys())

# sort
a = [5, 2, 3, 1, 4]
a.sort()
print(a)