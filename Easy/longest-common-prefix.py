# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        resultStr = ''
        
        for index, char in enumerate(strs[0]):
            for str in strs:
                if len(str) > index:
                    if str[index] != char:
                        return resultStr
                else: 
                    return resultStr
            
            resultStr += char
        return resultStr