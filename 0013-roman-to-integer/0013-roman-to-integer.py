class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
                        'C': 100, 'D': 500, 'M': 1000}
        index = 0
        total_sum = 0

        while index < len(s):
            # Check if the next character exists and forms a valid subtractive pair
            if index + 1 < len(s) and s[index] == 'C' and s[index + 1] == 'M':
                total_sum += 900
                index += 2
            elif index + 1 < len(s) and s[index] == 'X' and s[index + 1] == 'C':
                total_sum += 90
                index += 2
            elif index + 1 < len(s) and s[index] == 'I' and s[index + 1] == 'V':
                total_sum += 4
                index += 2
            elif index + 1 < len(s) and s[index] == 'C' and s[index + 1] == 'D':
                total_sum += 400
                index += 2
            elif index + 1 < len(s) and s[index] == 'X' and s[index + 1] == 'L':
                total_sum += 40
                index += 2
            elif index + 1 < len(s) and s[index] == 'I' and s[index + 1] == 'X':
                total_sum += 9
                index += 2
            else:
                total_sum += symbol_value[s[index]]
                index += 1

        return total_sum
