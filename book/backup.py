import numpy as np

junsupN = int(input())
arr = []


for i in range(junsupN):
   xn, yn = map(int, input().split())
   arr.append([xn, yn])

print(arr)
maxnum = max(np.array(arr).flatten().tolist())
num_range = maxnum - 1   # 좌표의 범위
arr_range = [0 for _ in range(num_range)]  


for i in arr:
   for j in range(i[0]-1,i[1]-1):
      arr_range[j] = 1

result = arr_range.count(1)

print(result)