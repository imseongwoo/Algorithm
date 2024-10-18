num_lst = [1, 2, 5, 3, 9, 6, 5, 3, 2]

stree = [0 for x in range(4 * len(num_lst))]


def merge(left, right):
    return left + right


# node : 현재 탐색하고 있는 노드 번호, left,right : node의 적용 범위 즉 노드에는 num_lst의 left부터 right번 까지 숫자의 합이 들어있음
def build(stree, node, left, right):
    # leaf node
    if left == right:
        stree[node] = num_lst[left]
        return stree[node]

    mid = left + (right - left) // 2
    left_val = build(stree, 2 * node, left, mid)
    right_val = build(stree, 2 * node + 1, mid + 1, right)
    stree[node] = merge(left_val, right_val)
    return stree[node]




build(stree,1,0,len(num_lst)-1)