n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
 
merged = []
first = 0
second = 0
 
while first < len(list1) and second < len(list2):
  if list1[first] <= list2[second]:
    merged.append(list1[first])
    first += 1
  else:
    merged.append(list2[second])
    second += 1
 
merged.extend(list1[first:])
merged.extend(list2[second:])
 
result = " ".join(map(str, merged))
print(result)
