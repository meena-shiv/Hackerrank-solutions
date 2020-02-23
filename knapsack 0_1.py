def knapsack(arr, max_sum):
  if len(arr) == 0 or max_sum == 0:
    return 0
  
  if max_sum < min(arr):
    return 0
  
  for element in arr:
    if max_sum % element == 0:
      return max_sum

  cache = [0] * (max_sum + 1)
  max_found_sum = 0
  for i in range(1, max_sum + 1):
    for val in arr:
      if i - val == 0 or i - val > 0 and cache[i - val] == 1:
        cache[i] = 1
        max_found_sum = i
  
  return max_found_sum 

tests = int(input())
for i in range(tests):
  _, max_sum = map(int, input().strip().split(" "))
  arr = [int(x) for x in input().strip().split(" ")]
  print(knapsack(arr, max_sum))
