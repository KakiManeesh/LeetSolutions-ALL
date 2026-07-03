# Last updated: 7/3/2026, 12:49:35 PM
class Solution:
    def isValid(self, word: str) -> bool:
        
        if len(word) < 3 :
            return False
        if not word.isalnum():
            return False
            
        vowels = {'a', 'e', 'i', 'o', 'u'}

        '''

        for char in word:
            if char.lower() in vowels:
                vowelcheck = True
            elif char.isalpha():
                conscheck = True            
            if vowelcheck and conscheck:
                return True
        
        return False

        '''
        stringset = set(list(word.lower()))
        
        if not  len(vowels & stringset) :
            return False
        consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}

        if not len(consonants & stringset ) :
            return False
        
        return True
        