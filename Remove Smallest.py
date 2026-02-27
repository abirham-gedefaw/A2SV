t = int(input())

for _ in range(t):
  size = int(input())
  nums = list(map(int, input().split()))
  nums.sort()

  flag = True

  for i in range(size - 1):
    if nums[i + 1] - nums[i] > 1:
      flag = False
  
  print("YES" if flag else "NO")
