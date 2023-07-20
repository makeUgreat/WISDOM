dice_1, dice_2, dice_3 = map(int, (input().split()))

price = 0

if 1 <= dice_1 <=6 and 1<= dice_2 <=6 and 1<= dice_3 <=6:
  
  if dice_1 == dice_2 == dice_3:
    price = 10000 + (dice_1 * 1000)

  elif dice_1 == dice_2 or dice_1 == dice_3:
    price = 1000 + (dice_1 * 100)
  
  elif dice_2 == dice_3:
    price = 1000 + (dice_2 * 100)

  else:
    numbers = [dice_1, dice_2, dice_3]
    max_value = numbers[0]
    for i in numbers:
      if i > max_value:
        max_value = i
  
    if dice_1 == max_value:
      price = dice_1 * 100
    
    elif dice_2 == max_value:
      price = dice_2 * 100
    
    elif dice_3 == max_value:
      price = dice_3 * 100

  print(price)
    
else:
  pass                             
                          

