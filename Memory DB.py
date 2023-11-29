# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 19:16:34 2023

@author: Yang Cairong
"""
from itertools import groupby
from concurrent.futures import ThreadPoolExecutor
import time

class MemoryDatabase:
    def __init__(self):
        self.records = {}
        self.indexes = {}  # 索引字典，键为字段名，值为该字段的索引
        self.transactions = []  # 事务列表，用于存储操作的记录

    def create_record(self, record_id):
        if record_id in self.records:
            raise ValueError(f"Record with id '{record_id}' already exists.")
        self.records[record_id] = {}

    def delete_record(self, record_id):
        if record_id not in self.records:
            raise ValueError(f"Record with id '{record_id}' does not exist.")
        del self.records[record_id]

    def create_field(self, record_id, field_name):
        if record_id not in self.records:
            raise ValueError(f"Record with id '{record_id}' does not exist.")
        if field_name in self.records[record_id]:
            raise ValueError(f"Field '{field_name}' already exists in record '{record_id}'.")
        self.records[record_id][field_name] = None

    def delete_field(self, record_id, field_name):
        if record_id not in self.records:
            raise ValueError(f"Record with id '{record_id}' does not exist.")
        if field_name not in self.records[record_id]:
            raise ValueError(f"Field '{field_name}' does not exist in record '{record_id}'.")
        del self.records[record_id][field_name]

    def set_value(self, record_id, field_name, value):
     
        #transaction
        if record_id not in self.records:
            raise ValueError(f"Record with id '{record_id}' does not exist.")
        if field_name not in self.records[record_id]:
            raise ValueError(f"Field '{field_name}' does not exist in record '{record_id}'.")
        # 在事务中添加操作
        if self.transactions:
            self.transactions[-1].append(lambda: self._set_value(record_id, field_name, value))

            
        
         # 更新字段索引
        elif field_name in self.indexes:
             if self.records[record_id][field_name] is not None:
                 # 从旧索引中移除记录的 ID
                 old_value = self.records[record_id][field_name]
                 self.indexes[field_name].get(old_value, []).remove(record_id)
             # 将记录的 ID 加入新索引中
             self.indexes[field_name].setdefault(value, []).append(record_id)
        else:
            self._set_value(record_id, field_name, value) 
            
            
            
            
            

    def get_value(self, record_id, field_name):
        if record_id not in self.records:
            raise ValueError(f"Record with id '{record_id}' does not exist.")
        if field_name not in self.records[record_id]:
            raise ValueError(f"Field '{field_name}' does not exist in record '{record_id}'.")
        return self.records[record_id][field_name]

# # Example usage
# db = MemoryDatabase()

# db.create_record(1)
# db.create_field(1, "name")
# db.create_field(1, "age")

# db.set_value(1, "name", "John")
# db.set_value(1, "age", 30)

# print(db.get_value(1, "name"))  # Output: John
# print(db.get_value(1, "age"))   # Output: 30

# db.delete_field(1, "age")

# print(db.get_value(1, "age"))   # Raises ValueError: Field 'age' does not exist in record '1'

# db.delete_record(1)
# print(db.get_value(1, "name"))  # Raises ValueError: Record with id '1' does not exist.




    # 其他方法（如 create_record, delete_record, create_field 等）省略...

    def query_records(self, condition):
        """
        根据条件查询数据库中的记录
        :param condition: 字典类型的条件，如 {'name': 'John', 'age': 30}
        :return: 符合条件的记录列表
        """
        result = []
        for record_id, record in self.records.items():
            matched = True
            for key, value in condition.items():
                if key not in record or record[key] != value:
                    matched = False
                    break
            if matched:
                result.append(record)
        return result

# # Example usage
# db = MemoryDatabase()

# db.create_record(1)
# db.create_field(1, "name")
# db.create_field(1, "age")

# db.set_value(1, "name", "John")
# db.set_value(1, "age", 30)

# db.create_record(2)
# db.create_field(2, "name")
# db.create_field(2, "age")

# db.set_value(2, "name", "Alice")
# db.set_value(2, "age", 25)

# # 查询年龄为30岁的记录
# condition = {'age': 30}
# result = db.query_records(condition)
# print(result)  # Output: [{'name': 'John', 'age': 30}]

# # 查询名字为'Alice'的记录
# condition = {'name': 'Alice'}
# result = db.query_records(condition)
# print(result)  # Output: [{'name': 'Alice', 'age': 25}]

# # 查询名字为'Bob'的记录（不存在）
# condition = {'name': 'Bob'}
# result = db.query_records(condition)
# print(result)  # Output: []



    def sort_records(self, field_name, reverse=False):
        """
        根据指定的字段对数据库中的记录进行排序
        :param field_name: 字段名，根据该字段进行排序
        :param reverse: 是否降序，默认为 False（升序）
        :return: 排序后的记录列表
        """
        if not self.records:
            return []

        if field_name not in next(iter(self.records.values())):
            raise ValueError(f"Field '{field_name}' does not exist in records.")

        # 使用 sorted() 函数对记录进行排序
        sorted_records = sorted(self.records.values(), key=lambda x: x.get(field_name), reverse=reverse)
        return sorted_records

# # Example usage
# db = MemoryDatabase()

# db.create_record(1)
# db.create_field(1, "name")
# db.create_field(1, "age")

# db.set_value(1, "name", "John")
# db.set_value(1, "age", 30)

# db.create_record(2)
# db.create_field(2, "name")
# db.create_field(2, "age")

# db.set_value(2, "name", "Alice")
# db.set_value(2, "age", 25)

# # 按年龄升序排序
# sorted_records = db.sort_records("age")
# print(sorted_records)
# # Output: [{'name': 'Alice', 'age': 25}, {'name': 'John', 'age': 30}]

# # 按名字降序排序
# sorted_records = db.sort_records("name", reverse=True)
# print(sorted_records)
# # Output: [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]



    # 其他方法（如 create_record, delete_record, create_field 等）省略...

    def group_records(self, field_name):
        """
        根据指定的字段对数据库中的记录进行分组
        :param field_name: 字段名，根据该字段进行分组
        :return: 分组后的记录字典，键为字段值，值为相应的记录列表
        """
        if not self.records:
            return {}

        if field_name not in next(iter(self.records.values())):
            raise ValueError(f"Field '{field_name}' does not exist in records.")

        # 使用 groupby() 函数对记录进行分组
        sorted_records = sorted(self.records.values(), key=lambda x: x.get(field_name))
        grouped_records = {k: list(g) for k, g in groupby(sorted_records, key=lambda x: x.get(field_name))}
        return grouped_records

# # Example usage
# db = MemoryDatabase()

# db.create_record(1)
# db.create_field(1, "name")
# db.create_field(1, "age")

# db.set_value(1, "name", "John")
# db.set_value(1, "age", 30)

# db.create_record(2)
# db.create_field(2, "name")
# db.create_field(2, "age")

# db.set_value(2, "name", "Alice")
# db.set_value(2, "age", 25)

# # 按名字字段分组
# grouped_records = db.group_records("name")
# print(grouped_records)
# # Output: {'Alice': [{'name': 'Alice', 'age': 25}], 'John': [{'name': 'John', 'age': 30}]}

# # 按年龄字段分组
# grouped_records = db.group_records("age")
# print(grouped_records)
# # Output: {25: [{'name': 'Alice', 'age': 25}], 30: [{'name': 'John', 'age': 30}]}

 # 其他方法（如 delete_record, create_field, set_value 等）省略...

    def begin_transaction(self):
        """
        开始一个新的事务
        """
        self.transactions.append([])

    def commit_transaction(self):
        """
        提交事务，将事务中的操作应用到数据库
        """
        if not self.transactions:
            raise ValueError("No transaction in progress.")
        for action in self.transactions[-1]:
            action()
        self.transactions.pop()

    def rollback_transaction(self):
        """
        回滚事务，撤销事务中的操作
        """
        if not self.transactions:
            raise ValueError("No transaction in progress.")
        self.transactions.pop()

    # def set_value(self, record_id, field_name, value):
    #     if record_id not in self.records:
    #         raise ValueError(f"Record with id '{record_id}' does not exist.")
    #     if field_name not in self.records[record_id]:
    #         raise ValueError(f"Field '{field_name}' does not exist in record '{record_id}'.")
    #     # 在事务中添加操作
    #     if self.transactions:
    #         self.transactions[-1].append(lambda: self._set_value(record_id, field_name, value))
    #     else:
    #         self._set_value(record_id, field_name, value)

    def _set_value(self, record_id, field_name, value):
        # 更新字段索引
        if field_name in self.indexes:
            if self.records[record_id][field_name] is not None:
                # 从旧索引中移除记录的 ID
                old_value = self.records[record_id][field_name]
                self.indexes[field_name].get(old_value, []).remove(record_id)
            # 将记录的 ID 加入新索引中
            self.indexes[field_name].setdefault(value, []).append(record_id)
        self.records[record_id][field_name] = value

# # Example usage
# db = MemoryDatabase()

# db.create_record(1)
# db.create_field(1, "name")
# db.create_field(1, "age")

# db.set_value(1, "name", "John")
# db.set_value(1, "age", 30)

# # 开始一个事务
# db.begin_transaction()

# # 在事务中进行修改，此时修改不会立即生效
# db.set_value(1, "name", "Alice")
# db.set_value(1, "age", 25)

# # 输出事务前的记录
# print(db.get_value(1, "name"))  # Output: John
# print(db.get_value(1, "age"))   # Output: 30

# # 提交事务，修改生效
# db.commit_transaction()

# # 输出事务后的记录
# print(db.get_value(1, "name"))  # Output: Alice
# print(db.get_value(1, "age"))   # Output: 25



    # 并发



    def concurrent_set_value(self, record_id, field_name, value):
        """
        并发设置字段值的方法
        """
        with ThreadPoolExecutor() as executor:
            future = executor.submit(self.set_value, record_id, field_name, value)
            return future.result()

# Example usage
db = MemoryDatabase()

db.create_record(1)
db.create_field(1, "name")
db.create_field(1, "age")

db.set_value(1, "name", "John")
db.set_value(1, "age", 30)

def concurrent_task():
    # 并发设置字段值
    db.concurrent_set_value(1, "name", "Alice")
    db.concurrent_set_value(1, "age", 25)

# 并发执行 concurrent_task
concurrent_task()

# 输出并发设置后的结果
print(db.get_value(1, "name"))  # Output: Alice
print(db.get_value(1, "age"))   # Output: 25







class MemoryDatabaseIndex:
    def __init__(self):
        self.records = {}
        self.indexes = {}  # 索引字典，键为字段名，值为该字段的索引

    def create_record(self, record_id):
        if record_id in self.records:
            raise ValueError(f"Record with id '{record_id}' already exists.")
        self.records[record_id] = {}

    # 其他方法（如 delete_record, create_field, set_value 等）省略...

    def create_field(self, record_id, field_name):
        if record_id not in self.records:
            raise ValueError(f"Record with id '{record_id}' does not exist.")
        if field_name in self.records[record_id]:
            raise ValueError(f"Field '{field_name}' already exists in record '{record_id}'.")
        self.records[record_id][field_name] = None
        # 创建字段索引
        if field_name not in self.indexes:
            self.indexes[field_name] = {}

    def set_value(self, record_id, field_name, value):
        if record_id not in self.records:
            raise ValueError(f"Record with id '{record_id}' does not exist.")
        if field_name not in self.records[record_id]:
            raise ValueError(f"Field '{field_name}' does not exist in record '{record_id}'.")
        # 更新字段索引
        if field_name in self.indexes:
            if self.records[record_id][field_name] is not None:
                # 从旧索引中移除记录的 ID
                old_value = self.records[record_id][field_name]
                self.indexes[field_name].get(old_value, []).remove(record_id)
            # 将记录的 ID 加入新索引中
            self.indexes[field_name].setdefault(value, []).append(record_id)
        self.records[record_id][field_name] = value

    def query_by_index(self, field_name, value):
        """
        根据字段索引快速查询记录
        :param field_name: 字段名
        :param value: 字段的值
        :return: 符合条件的记录列表
        """
        if field_name not in self.indexes:
            raise ValueError(f"Field '{field_name}' does not have an index.")
        return [self.records[record_id] for record_id in self.indexes[field_name].get(value, [])]

# # Example usage
# db = MemoryDatabaseIndex()

# db.create_record(1)
# db.create_field(1, "name")
# db.create_field(1, "age")

# db.set_value(1, "name", "John")
# db.set_value(1, "age", 30)

# db.create_record(2)
# db.create_field(2, "name")
# db.create_field(2, "age")

# db.set_value(2, "name", "Alice")
# db.set_value(2, "age", 25)

# # 创建字段 name 和 age 的索引后，可以通过索引快速查询记录
# result = db.query_by_index("name", "John")
# print(result)  # Output: [{'name': 'John', 'age': 30}]

# result = db.query_by_index("age", 25)
# print(result)  # Output: [{'name': 'Alice', 'age': 25}]

# result = db.query_by_index("age", 40)
# print(result)  # Output: []





   