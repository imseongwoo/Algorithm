
alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

n = input()

for i in alpha:
    n=n.replace(i,'_')

print(len(n))
