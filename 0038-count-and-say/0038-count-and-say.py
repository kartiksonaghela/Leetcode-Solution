class Solution:
    def countAndSay(self, n: int) -> str:
        # Start with the base case
        result = "1"

        # Loop to build each term up to the nth term
        for _ in range(n - 1):
            current_term = result
            next_term = ""
            i = 0

            # Count consecutive characters in the current term
            while i < len(current_term):
                count = 1  # Start counting from 1
                # Count how many times the same digit repeats consecutively
                while i + 1 < len(current_term) and current_term[i] == current_term[i + 1]:
                    count += 1
                    i += 1
                # Append the count and the digit to form the next term
                next_term += str(count) + current_term[i]
                i += 1

            # Update result to be the next term for the next iteration
            result = next_term

        return result
