class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Si tienen distinta longitud, no anagramas
        if len(s) != len(t):
            return False
        
        conteo = {}
        
        # Recorro la primera palabra y cuento cada letra
        for letra in s:
            if letra in conteo:
                conteo[letra] += 1   # Si ya existe
            else:
                conteo[letra] = 1    # Si no existe
        
        # Recorro la segunda palabra y resto cada letra
        for letra in t:
            if letra in conteo:
                conteo[letra] -= 1  
            else:
                return False         # Letra que no estaba en s, imposible anagrama
        
        # Comprueba que todos los valores son 0
        for valor in conteo.values():
            if valor != 0:
                return False
        
        return True

# Pruebas
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))  # → True
print(sol.isAnagram("rat", "car"))          # → False
