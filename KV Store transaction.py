# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:30:42 2023

@author: Yang Cairong
"""

from collections import defaultdict

class KVStore:
    def __init__(self):
        self.txid = 0
        self.actual_data = {}
        self.tx_data = defaultdict(list)

    def begin(self):
        self.txid += 1
        return self.txid

    def read(self, txid, key):
        if key in self.tx_data and len(self.tx_data[key]) > 1:
            raise Exception("Value is written by multiple transactions")
        
        if key in self.tx_data:
            return self.tx_data[key][0][0]
        elif key in self.actual_data:
            return self.actual_data[key]
        else:
            return None

    def write(self, txid, key, val):
        if key in self.tx_data and txid != self.tx_data[key][0][1]:
            raise Exception("Value is written by another transaction")

        self.tx_data[key] = [(val, txid)]

    def commit(self, txid):
        keys_to_remove = []
    
        for key, val_list in self.tx_data.items():
            for val, version in val_list:
                if version == txid:
                    self.actual_data[key] = val
            keys_to_remove.append(key)
    
        for key in keys_to_remove:
            del self.tx_data[key]


# 示例用法
kv = KVStore()
tx1 = kv.begin()
kv.write(tx1, "name", "Alice")
kv.write(tx1, "age", 30)
kv.commit(tx1)

tx2 = kv.begin()
kv.write(tx2, "name", "Bob")
print(kv.read(tx2, "name"))  # 输出 "Bob"
print(kv.read(tx2, "age"))   # 输出 30
