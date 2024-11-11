class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list=[]
        nums=strs
        anagram_dict = defaultdict(list)
        for word in nums:
            print(word)
            # Sort the characters in the word and use as key
            sorted_word = tuple(sorted(word))
            anagram_dict[sorted_word].append(word)
        # Convert the dictionary values to a list of lists
        return list(anagram_dict.values())