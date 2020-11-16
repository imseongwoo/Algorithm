# # 유클리드 호제법
# def gcd(x:int,y:int)-> int:
#     if x%y==0:
#         return y
#     else:
#         return gcd(y,x%y)
#
#
# x=int(input())
# y=int(input())
# print(gcd(x,y))
#-------------------------------------------------------------------

def move(no:int,x:int,y:int)->None:
    """원반 no개를 x기둥에서 y기둥으로 옮김"""
    if no>1:
        move(no-1,x,6-x-y)                          # 기둥 번호의 합이 6ㅣ므로 시작기둥,목표기둥이 어느 위치에 있든 중간 기둥은 6-x-y 로 구할 수 있다.
    print(f'원반 [{no}]를 {x}기둥에서{y}기둥으로 옮깁니다.')

    if no>1:
        move(no-1,6-x-y,y)

print('하노이의 탑을 구현합니다.')
n = int(input('원반의 개수를 입력하세요:'))

move(n,1,3)