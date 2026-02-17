class Solution:
    def isPalindrome(self, s: str) -> bool:
       s=s.lower()
       #recorro caracteres de s y me quedo con letras y numeros en una nueva cadena
       s = ''.join(c for c in s if c.isalnum())
       t=s[::-1]
       if t==s:
           return True
       else:
           return False
       



sol = Solution()

print(sol.isPalindrome("racecar"))                       # → True
print(sol.isPalindrome("hello"))                         # → False
print(sol.isPalindrome("A man, a plan, a canal: Panama"))# → True
print(sol.isPalindrome("race a car"))                    # → False
print(sol.isPalindrome(" "))                             # → True (cadena vacía tras limpiar)