from typing import List

def son_anagramas(palabra1, palabra2):
    conteo = {}
    
    for letra in palabra1:
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1
    
    for letra in palabra2:
        if letra in conteo:
            conteo[letra] -= 1
        else:
            return False
    
    for valor in conteo.values():
        if valor != 0:
            return False
    
    return True

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupos = []
        
        for palabra in strs:
            colocada = False
            
            for grupo in grupos:
                if son_anagramas(palabra, grupo[0]):
                    grupo.append(palabra)
                    colocada = True
                    break
            
            if not colocada:
                grupos.append([palabra])
        
        return grupos

sol = Solution()

entrada1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Test 1:", sol.groupAnagrams(entrada1))

entrada2 = ["abc", "bca", "cab", "cba"]
print("Test 2:", sol.groupAnagrams(entrada2))

entrada3 = ["hola", "mundo", "python"]
print("Test 3:", sol.groupAnagrams(entrada3))

entrada4 = ["unico"]
print("Test 4:", sol.groupAnagrams(entrada4))