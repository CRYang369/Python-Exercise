# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 18:19:07 2023

@author: Yang Cairong
"""


class BinaryHeapIdAllocater:
    def __init__(self):
        self.kMaxID =8
        self.kMaxIndex = self.kMaxID * 2
        self.ids_state = [False] * self.kMaxIndex
        self.root_index = 1

    def get_index_from_id(self, id):
        if id < 0 or id == self.kMaxID:
            return f"{id}out of the maxID"
        return self.kMaxID +id

    def get_id_from_index(self, index):
        return index -self. kMaxID

    def update_tree(self, cur_index):
        while cur_index >self.root_index:
            cur_index = cur_index // 2
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1

            if self.ids_state[left_child_index] and self.ids_state[right_child_index]:
                self.ids_state[cur_index] = True
            else:
                self.ids_state[cur_index] = False

    def allocate(self):
        cur_index = self.root_index
        if self.ids_state[cur_index] :        
            return f'index {cur_index} has been allocated'      # index 1 has been allocated
        #That means all the leaves have been allocated and updated the root to be true(allocated)

        while cur_index * 2+1 < self.kMaxIndex:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1

            if not self.ids_state[left_child_index]:
                cur_index = left_child_index
            elif not self.ids_state[right_child_index]:
                cur_index = right_child_index
            else:
                return -1

        id = self.get_id_from_index(cur_index)
        self.ids_state[cur_index] = True
        self.update_tree(cur_index)
        return f'{id} allocated'

    # def release(self, id):
    #     index = self.get_index_from_id(id)

    #     if id < 0:
    #         return False

    #     self.ids_state[index] = False
    #     self.update_tree(index)
    #     return f'{id} released'
    def release(self, id):
        cur_index = self.get_index_from_id(id)
    
        if id < 0:
            return False
    
        self.ids_state[cur_index] = False
        self.update_tree(cur_index)
        return f'{id} released'

        # if  0 > index  or index> self.kMaxIndex or self.ids_state[index] == False:
        #     raise Exception(f"The allocatedId {id} cannot be released.")
        # self.ids_state[index] = False
        # self.update_tree(index)
        # return f'{id} released'

# Testing the BinaryHeapIdAllocater class
allocator = BinaryHeapIdAllocater()
print(allocator.allocate())  # Output: 0
print(allocator.allocate())  # Output: 1
print(allocator.release(0))  # Output: 0 released
print(allocator.allocate())  # Output: 0 (Reallocated)
print(allocator.release(1))  # Output: 1 released
print(allocator.allocate())  # Output: 1 (Reallocated)
print(allocator.allocate())  # Output: 2 (Next available ID)
print(allocator.allocate())  # Output: 2 (Next available ID)
print(allocator.allocate())  # Output: 2 (Next available ID)
print(allocator.allocate())  # Output: 2 (Next available ID)
print(allocator.allocate())  # Output: 2 (Next available ID)
print(allocator.allocate())  # Output: 2 (Next available ID)
print(allocator.allocate())  # Output: 2 (Next available ID)

