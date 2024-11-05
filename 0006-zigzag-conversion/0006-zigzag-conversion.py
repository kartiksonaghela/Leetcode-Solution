class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lists = [[] for _ in range(numRows)]
        counter = 0

        if numRows == 1:
            return s
        else:
            while counter < len(s):
                # Vertical downward movement
                for i in range(numRows):
                    if counter < len(s):
                        lists[i].append(s[counter])
                        counter += 1
                    else:
                        break

                # Diagonal upward movement (from second-last row up to the second row)
                for j in range(numRows - 2, 0, -1):
                    if counter < len(s):
                        lists[j].append(s[counter])
                        counter += 1
                    else:
                        break

        # Combine all rows to form the final output
        return ''.join([''.join(row) for row in lists])