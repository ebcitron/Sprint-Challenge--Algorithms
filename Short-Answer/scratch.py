def scratch(n):
    sum = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            sum += 1
            print(range(n))
            print(sum, j, n)

ops = 0
def bunnyEars(bunnies):
       
      if bunnies == 0:
        return 0
    
      
      return 2 + bunnyEars(bunnies-1)
      print(ops)
    
print(bunnyEars(40))
