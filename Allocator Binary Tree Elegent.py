# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 18:14:38 2023

@author: Yang Cairong
"""

class CannotAllocateException(Exception):
    pass


class InvalidIdException(Exception):
    pass


class BinaryHeapAllocator:

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.bool_array = [False] * (2 * max_capacity)
# we need a binary tree to mimic a heap,use the bottom leaves node to store the 
# allocation state, so use the property of a binary tree we need the same size 
# as the leaves to perserve the path of the tree.

    def allocate(self):
        """Returns an unallocated id"""
        index = 0
# When all the leaves have been allocated,they will update their allocated
# state from bottom to up till the root node. 
        if self.bool_array[index]:
             raise CannotAllocateException("No ids available")
#we need to check the children nodes of each index within the proper range 
# till reach the leaf nodes           
        while 2*index+2 < len( self.bool_array):
             left_child_index = index * 2 + 1
             right_child_index = index * 2 + 2
# check the state of the left and right child to update the index into 
# the one with free space to allocate or availability  
             if not self.bool_array[left_child_index]:
                 index = left_child_index
             elif not self.bool_array[right_child_index]:
                 index = right_child_index
             else: #Both subtrees are allocated,the current index can't be allocated neither
                 raise CannotAllocateException("No ids available")
  
        self.bool_array[index] = True
        self.update_tree(index)
        allocate_id = self.get_id_from_index(index)
        # print(f'{id} allocated')
        return allocate_id


    def release(self, release_id):
        """Releases the id and allows it to be allocated"""
        index = self.get_index_from_id(release_id)
        if not 0 <= release_id < self.max_capacity or not self.bool_array[index]  :
            raise InvalidIdException(f"The id {id} cannot be released.")
            
        self.bool_array[index] = False
        self.update_tree(index)
        # print(f'{release_id} has been released' )
        # return release_id
  
# index=id+(max_capacity-1)  
# id starts from the root node following the order parent->left->right order (BFS)
    def get_index_from_id(self, node_id): # All leaf nodes at the bottom level of the tree
        return node_id + self.max_capacity - 1
#id=index-(max_capaxity-1)    
# id starts from the  leftmost node among the leaf nodes at the bottom of the tree
    def get_id_from_index(self, index):
        return index - self.max_capacity + 1   
    
    def update_tree(self, index):
        while index > 0: # we need use this index as a child node to find it's parent
            index = (index-1)// 2 # the index will change into left or right child
            left_child_index = index * 2 + 1
            right_child_index = index * 2 + 2
# the node is unavailable(Ture) if both children are unavailable(Ture)
            if self.bool_array[left_child_index] and self.bool_array[right_child_index]:
                self.bool_array[index] = True
            else:
                self.bool_array[index] = False
    

# Test the IDAllocator class
allocator = BinaryHeapAllocator(8)

print(allocator.allocate())  # Output: 0
print(allocator.allocate())  # Output: 1
allocator.release(0)  # Output: 0 released
print(allocator.allocate())  # Output: 0 (Reallocated)
allocator.release(1) # Output: 1 released
# print(allocator.release(5))  # Output: InvalidIdException: The id 5 cannot be released.
print(allocator.allocate())  # Output: 1 (Reallocated)
print(allocator.allocate())  # Output: 2 (Next available ID)
print(allocator.allocate())  # Output: 2 (Next available ID)
print(allocator.allocate())  # Output: 2 (Next available ID)
print(allocator.allocate())  # Output: 2 (Next available ID)
print(allocator.allocate())  # Output: 2 (Next available ID)
allocator.release(1)
print(allocator.allocate())  # Output: 2 (Next available ID)
print(allocator.allocate())  # Output: CannotAllocateException: No ids available
print(allocator.allocate())  # Output: CannotAllocateException: No ids available

