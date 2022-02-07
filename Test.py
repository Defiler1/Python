def ascending(ns):
   if len(ns) < 2:
      return False
   else:
      while len(ns) >= 2:
         if ns[0] < ns[1]:
            ns = ns[1:]
         else:
            return False
      return True

# print(ascending([3,1,2])) 



def sublists(ns):
    def get(k,ns):
        subs = []
        for i in range(len(ns)-k+1):
            subs.append(ns[i:i+k])
        return subs
    subs = [[]]
    for k in range(1,len(ns)):
        subs += get(k,ns)
    if ns != []:
        subs.append(ns)
    return subs


# print(sublists([3,1,2])) 
# [[], [3], [1], [2], [3, 1], [1, 2], [3, 1, 2]]


# print(ascending_sublists([3,1,2])) 
# # [[1, 2]]