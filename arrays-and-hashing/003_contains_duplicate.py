from collections import Counter
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq=Counter(nums)
        for cantidad in freq.values():
            if cantidad > 1:
                return True
        
        return False

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visto=set()
        for num in nums:

            if num in visto:
                return True
            visto.add(num)
    
        return False
    


sol1 = Solution()
sol2 = Solution2()

print(sol1.hasDuplicate([1, 2, 3, 1]))   # → True
print(sol1.hasDuplicate([1, 2, 3, 4]))   # → False
print(sol1.hasDuplicate([1, 1, 1, 3]))   # → True

print(sol2.containsDuplicate([1, 2, 3, 1]))  # → True
print(sol2.containsDuplicate([1, 2, 3, 4]))  # → False
print(sol2.containsDuplicate([1, 1, 1, 3]))  # → True