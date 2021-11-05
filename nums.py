find_missing_nums(nums)
class Solution:
   def solve(self, nums):
      arr = [0]*(len(nums)+1)
      for i in nums:
         arr[i] += 1
      missing = []
      for i in range(len(arr)):
         if arr[i] == 0 and i != 0:
            missing.append(i)
      return missing
ob = Solution()
print(ob.solve([4, 4, 2, 2, 6, 6]))