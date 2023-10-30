def calculate_average(x, y):
  sum_of_evens = 0
  count_of_evens = 0
  for num in range(x, y + 1):
      if num % 2 == 0:
          sum_of_evens += num
          count_of_evens += 1
  if count_of_evens == 0:
      return 0  
  else:
      return sum_of_evens / count_of_evens
