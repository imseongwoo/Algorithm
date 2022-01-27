n = int(input())

def dp(len):
    if d[len] > 0 :
        return d[len]

    if len == 1 or len == 2 :
        return len

    else:
        d[len] = dp(len-2) + dp(len-1)
        return d[len]





d = [0] * (n+1)
print(dp(n))