class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # Dictionary mapping digits to letters
        dict1 = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        # Input digits
        input_digits = digits
        if len(input_digits):
            # Get the corresponding lists of letters for each digit in the input
            letter_groups = [dict1[digit] for digit in input_digits if digit in dict1]

            # Generate all combinations
            combinations = [''.join(combo) for combo in product(*letter_groups)] 

            return combinations
        else:
            return []