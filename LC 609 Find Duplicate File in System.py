# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:41:40 2023

@author: Yang Cairong
"""
from collections import defaultdict
class Solution:
    def findDuplicate(self,paths):
        content_to_path=defaultdict(list)
        for path in paths:
            path_list=path.split(" ")
            for f in path_list[1:]:
                open_bracket=f.index("(")
                close_bracket=f.index(")")
                content=f[open_bracket+1:close_bracket]
                out_path=path_list[0]+"/"+f[:open_bracket]
                content_to_path[content].append(out_path)
        return [dup for dup in content_to_path.values() if len(dup)>1]
                
                
                
if __name__=="__main__":
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
 # Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
    test=Solution()
    print( test.findDuplicate(paths))