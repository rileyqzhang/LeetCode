class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''
        Iterate through s, and keep a window size of 10 open
        Use a dictionary to check if each substring has appeared
        Use a list to store the results
        '''
        seen = defaultdict(int)
        result = []       

        for left in range(len(s)-10+1):
            seen[s[left:left+10]] += 1

        for key,value in seen.items():
            if value > 1:
                result.append(key)
        
        return result
        

            
                
            







        