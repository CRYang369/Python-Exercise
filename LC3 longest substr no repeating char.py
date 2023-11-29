
'''
Given a string, find the length of the longest substring without repeating characters.


Maintain a sliding window,updating the start whenever we see a character repeated.
Time O(n)
Space O(1),dictionary is limited by fixed size alphabet
'''
class Solution:
    def lengthOfLongestSubstring(self, s:str)->int:
        """
        :type s: [str]
        :rtype: int
        Maintain a sliding window,updating the start whenever we see a character repeated.
        """
        
        last_seen = {}
        start, longest= 0, 0

        for i,c in enumerate(s):
            if c in last_seen and last_seen[c]>=start:
                start=last_seen[c]+1
            else:
                longest=max(longest,i-start+1)
            last_seen[c]=i         
        return longest
    
if __name__=="__main__":
    test=Solution()
    slist='abcabcbb'
    # slist=['pwwkew','abc','abbc','bcca','abbccdda']
    res= test.lengthOfLongestSubstring(slist)
    print(res)
    