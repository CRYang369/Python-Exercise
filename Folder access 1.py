# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 09:32:44 2023

@author: Yang Cairong
"""
import collections 
class FolderAccess:

    def __init__(self, folder_to_parent, access):
        #folder_to_parent is a list (child folder, parent folder)
        #access is a set of folders that you have access to
        self.parent_to_childen = collections.defaultdict(list)
        self.access = access
        for child, parent in folder_to_parent:
            self.parent_to_childen[parent].append(child)
        self.process_folders()

    def process_folders(self):
        """Grants access to all children, allows for constant time access lookup, breadth-first"""
        current_access = set(self.access)
        while current_access:
            next_access = set()
            for file in current_access:
                children = self.parent_to_childen.get(file, None)
                if children is not None:
                    for child in children:
                        if child not in self.access:
                            next_access.add(child)
            self.access+=list(next_access)
            current_access = next_access

    def has_access(self, folder_name):
        return folder_name in self.access