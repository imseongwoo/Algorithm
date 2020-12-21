# import sys
#
#
# def push(a):
#     stk.append(a)
#
#
# def pop():
#     if not stk:
#         print(-1)
#     else:
#         print(int(stk.pop()))
#
#
# def size():
#     print(len(stk))
#
#
# def empty():
#     if not stk:
#         print(1)
#     else:
#         print(0)
#
#
# def top():
#     if not stk:
#         print(-1)
#     else:
#         print(stk[len(stk) - 1])
#
#
# stk = []  # 빈 스택
# a = eval(input())  # 커멘드 입력 횟수 입력
# for i in range(a):
#     command = sys.stdin.readline().split()
#     if command[0] == 'push':
#         push(command[1])
#     elif command[0] == 'pop':
#         pop()
#     elif command[0] == 'empty':
#         empty()
#     elif command[0] == 'size':
#         size()
#     elif command[0] == 'top':
#         top()
#
#
from collections import deque

a = deque(input())

print(a)