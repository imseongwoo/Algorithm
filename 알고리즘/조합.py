# 조합이란 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것
# 파이썬에서 조합을 이용하기 위해서는 itertools의 combinations() 함수 사용.

import itertools

data = [1,2,3]

for x in itertools.combinations(data,2):
    print(list(x))