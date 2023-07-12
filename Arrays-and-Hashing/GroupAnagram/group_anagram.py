from collections import defaultdict
from typing import List


# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_groups = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)

    return list(anagram_groups.values())
