# 1065

def check(numbers):

    if len(str(numbers))==1:
        return True
    elif len(str(numbers))==2:
        return True
    elif len(str(numbers))==3:
        if (numbers%100//10)-(numbers//100) == (numbers%100%10)-(numbers%100//10):
            return True
        else:
            return False
    else:
        return False
n = int(input())
count = 0
for i in range(1,n+1):
    if check(i)==True:
        count += 1

print(count)