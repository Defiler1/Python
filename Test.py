import sys

n, t, g = map(int, input().split())


def bfs(n, t, g):
   q, visited = [n], {n}
   step = 0
   while q:
      size = len(q)

      for i in range(size):
         cur = q.pop(0)
         if cur == g:
            return step

         if cur * 2 > 99999:
            next_move = [cur+1]
         else:
            m = list(str(cur*2))
            m[0] = str(int(m[0])-1) if int(m[0]) - 1 > 0 else str(0)
            # 결과 = A if 조건 else B
            # 조건이 True면 A False면 B 
            m = int("".join(m))
            next_move = [cur+1, m]

         for j in next_move:
            if j >= 0 and j <= 99999 and j not in visited:
               q.append(j)
               visited.add(j)
         step += 1

         if step > t:
            break
      return "ANG"

print(bfs(n, t, g))