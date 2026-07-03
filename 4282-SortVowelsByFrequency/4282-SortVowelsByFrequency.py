# Last updated: 7/3/2026, 12:54:57 PM
class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_freq = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0
        }
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        first_occurrence = {}
        
        # Count frequencies and track first occurrence position
        for i, char in enumerate(s):
            if char in vowel_freq:
                vowel_freq[char] += 1
                if char not in first_occurrence:
                    first_occurrence[char] = i
        
        # Sort vowels by:
        # 1. Frequency (descending)
        # 2. First occurrence position (ascending) as tiebreaker
        # Only include vowels that actually appear in the string
        sorted_vowels = sorted(
            [(v, f) for v, f in vowel_freq.items() if f > 0],
            key=lambda x: (-x[1], first_occurrence[x[0]])
        )
        
        # Create a queue/list of vowels in sorted order
        vowel_queue = []
        for vowel, freq in sorted_vowels:
            vowel_queue.extend([vowel] * freq)
        
        # Replace vowels in original string with sorted vowels
        result = []
        vowel_index = 0
        
        for char in s:
            if char in vowels:
                result.append(vowel_queue[vowel_index])
                vowel_index += 1
            else:
                result.append(char)
        
        return ''.join(result)