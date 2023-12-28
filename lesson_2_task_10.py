# x - это сумма вклада, y - это срок вклада в годах, 10% - ставка

def bank(x, y):
   for i in range (0, y):
      x = (x * 0.1) + x
   print(x)
bank(100, 4)