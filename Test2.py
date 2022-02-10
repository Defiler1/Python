n = int(input())

def coin_count(n):
   c500 = 0 
   c100 = 0 
   c50 = 0 
   c10 = 0 
   c5 = 0 
   c1 = 0 

   change = 1000 - n    # 받아야 하는 거스름돈

   c500 += int(change/500)
   change = change - (c500 * 500)
   
   c100 += int(change/100)
   change = change - (c100 * 100)

   c50 += int(change/50)
   change = change - (c50 * 50)
   
   c10 += int(change/10)
   change = change - (c10 * 10)
   
   c5 += int(change/5)
   change = change - (c5 * 5)

   c1 += int(change/1)
   change = change - (c1 * 1)

   count = c500 + c100 + c50 + c10 + c5 + c1

   return count

print(coin_count(n))
# a = int(input())


coinList = (500,100,50,10,5,1)
def coin_count2(n, coinList):
   count = 0
   change = 1000 - n
   for i in coinList:
      count += int(change/i)
      change -= int(change/i) * i
   return count

# print(coin_count2(a, coinList))

