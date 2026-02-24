from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resultado=[]
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                for k in range (j+1, len(nums)):
                    suma=nums[i]+nums[j]+nums[k]
                    if suma==0:
                        tripla= sorted([nums[i], nums[j], nums[k]])
                        if tripla not in resultado:
                            resultado.append(tripla)
        
        return resultado

sol = Solution()

print("Test 1:", sol.threeSum([-1, 0, 1, 2, -1, -4]))

print("Test 2:", sol.threeSum([0, 0, 0]))

print("Test 3:", sol.threeSum([1, 2, 3]))

print("Test 4:", sol.threeSum([-2, 0, 0, 2, 2]))

print("Test 5:", sol.threeSum([-1, 0, 1]))
