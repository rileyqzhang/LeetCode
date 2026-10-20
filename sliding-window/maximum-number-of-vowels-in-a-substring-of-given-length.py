class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        max_number = 0
        current_count = 0
        
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
                             
        max_number = current_count

        for r in range(k, len(s)):
            if s[r-k] in vowels :
                current_count -= 1

            if s[r] in vowels:
                current_count += 1
                max_number = max(max_number, current_count)
            
        return max_number
            
            

            
            
            

            


        
        