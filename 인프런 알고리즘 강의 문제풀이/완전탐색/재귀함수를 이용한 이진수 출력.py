def binary_print(n):
    if n > 1:
        ref.append(n % 2)
        return binary_print(n // 2)

    else:
        ref.append(n)
        return ref
n = int(input())

ref = []
a = binary_print(n)
a.reverse()

for x in a:
    print(x,end='')

# 답

def DFS(x):
    if x == 0:
        return      # 함수 종료
    else:
        DFS(x//2)      # 백트랙킹
        print(x%2,end='')


if __name__=="__main__":
    n=int(input())
    DFS(n)


# 재귀함수를 이용한 이진수 출력 복습
def dfs(v):
    if v!=0:
        dfs(v//2)
        print(v%2,end='')



n = int(input())
dfs(n)



























