s = input()

s = sorted(s,reverse=True)
sum =''
for i in range(len(s)):
    sum = sum + s[i]
print(sum)