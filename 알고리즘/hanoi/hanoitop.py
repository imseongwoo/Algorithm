n = int(input())

def hanoi_tower(n, fro,tmp,to):
    if n==1:
        print('1 : A->B')
        print('1 : B->C')
    else:
        hanoi_tower(n-1,fro,to,tmp)
        print('%d : %c->%c'%(n,fro,to))
        hanoi_tower(n-1,tmp,fro.to)
fromm='A'
tmpp='B'
too='C'
hanoi_tower(n,fromm,tmpp,too)