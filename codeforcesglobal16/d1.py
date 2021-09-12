# count
def InvCount(arr, n):
   inv_count = 0
   for i in range(n):
      for j in range(i + 1, n):
         if (arr[i] > arr[j]):
            inv_count += 1
   return inv_count

for case in range(int(input())):
    n, m = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    nums = nums[::-1]
    print(InvCount(nums, m))