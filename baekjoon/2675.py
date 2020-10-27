

word = input().upper()


# array=[]
# for c in range(ord('A'),ord('Z')+1):
#     array.append(word.count(chr(c)))
array = [word.count(chr(c)) for c in range(ord('A'),ord('Z')+1)]
maxnum = max(array)

if array.count(maxnum)==1:
    print(chr(array.index(maxnum)+ord('A')))
else:
    print('?')