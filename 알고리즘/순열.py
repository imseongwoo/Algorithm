import itertools

data = [1,2,3]

for x in itertools.permutations(data,2):
    print(list(x))

# 코딩 테스트에서는 경우의 수 값만 출력하는 것이 아니라 모든 경우를 다 출력하도록 요구하기도 하기때문에 파이썬의 itertools 라이브러리를 이용

