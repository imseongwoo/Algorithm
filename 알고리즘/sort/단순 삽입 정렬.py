from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    """단순 삽입 정렬"""
    n = len(a)
    for i in range(1,n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1]> tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

if __name__ == '__main__':
    print('단순 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요:'))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]:'))

    insertion_sort(x)

    print('오름차순으로 정렬')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

"""이 알고리즘은 서로 떨어져 있는 원소를 교환하지 않으므로 안정적이라고 할 수 있다.
    단순 정렬 알고리즘의 시간 복잡도는 모두 O(n^2)으로 프로그램의 효율이 좋지 않다."""
