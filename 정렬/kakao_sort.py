import re

arr = []
files = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']

for i in range(len(files)):

    arr.append(re.findall('(\D+)(\d+)(.*)', files[i])[0])

arr = sorted(arr, key=lambda x: (x[0].upper(), int(x[1])))
arr = list(map(''.join,arr))
print(arr)
