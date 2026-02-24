from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        izquierda=0
        derecha= len(numbers)-1

        while izquierda<derecha:
            suma=numbers[izquierda]+numbers[derecha]
            if suma ==target:
                return [izquierda+1,derecha+1]
            elif suma <target:
                izquierda+=1
            else:
                derecha -=1

sol = Solution()

print("Test 1:", sol.twoSum([2, 7, 11, 15], 9))

print("Test 2:", sol.twoSum([2, 3, 4], 6))

print("Test 3:", sol.twoSum([1, 2, 3, 4, 5], 9))

print("Test 4:", sol.twoSum([-3, -1, 0, 2, 4], 1))

print("Test 5:", sol.twoSum([1, 3], 4))
