# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:32:50 2023

@author: Yang Cairong
"""

def reverse_string(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

def reverse_ordering_of_words(s):
    # Convert the input string to a list of characters
    s_list = list(s)
    len_s = len(s_list)

    # Reverse the whole string
    reverse_string(s_list, 0, len_s - 1)

    word_beginning = 0
    # Find word boundaries and reverse word by word
    for word_end in range(len_s):
        if s_list[word_end] == ' ':
            reverse_string(s_list, word_beginning, word_end - 1)
            word_beginning = word_end + 1

    # Reverse the last word (if there is no space at the end)
    reverse_string(s_list, word_beginning, len_s - 1)

    # Convert the list of characters back to a string and return it
    return ''.join(s_list)

# Example usage:
s = "   word1  word2 "
print(reverse_ordering_of_words(s))  # Output: "Python World Hello"
