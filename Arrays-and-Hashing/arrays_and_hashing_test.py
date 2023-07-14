import unittest
import ContainsDuplicate.contains_duplicate as duplicate
import ValidAnagram.valid_anagram as valid_anagram
import TwoSum.two_sum as two_sum
import GroupAnagram.group_anagram as group_anagram
import TopKFrequent.top_k_frequent as top_k_frequent


class TestArraysAndHashing(unittest.TestCase):

    def testContainsDuplicate(self):
        self.assertTrue(duplicate.containsDuplicate(self, [1, 2, 3, 1]))
        self.assertFalse(duplicate.containsDuplicate(self, [1, 2, 3, 4]))
        self.assertTrue(duplicate.containsDuplicate(self, [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def testValidAnagram(self):
        self.assertTrue(valid_anagram.isAnagram(self, "anagram", "nagaram"))
        self.assertFalse(valid_anagram.isAnagram(self, "rat", "car"))

    def testTwoSum(self):
        self.assertEqual(list(two_sum.twoSum(self, [2, 7, 11, 15], 9)), [0, 1])
        self.assertEqual(list(two_sum.twoSum(self, [3, 2, 4], 6)), [1, 2])
        self.assertEqual(list(two_sum.twoSum(self, [3, 3], 6)), [0, 1])

    def testGroupAnagram(self):
        self.assertEqual(group_anagram.groupAnagrams(self,
                                                     ["eat", "tea", "tan", "ate", "nat", "bat"]),
                         [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
        self.assertEqual(group_anagram.groupAnagrams(self, [""]), [[""]])
        self.assertEqual(group_anagram.groupAnagrams(self, ["a"]), [["a"]])

    def testTopKFrequent(self):
        self.assertEqual(top_k_frequent.topKFrequent(self, [1, 1, 1, 2, 2, 3], 2), [1, 2])
        self.assertEqual(top_k_frequent.topKFrequent(self, [1], 1), [1])


if __name__ == '__main__':
    unittest.main()
