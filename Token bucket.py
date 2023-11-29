# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 18:34:08 2023

@author: Yang Cairong
"""

import time
import threading
import random

class TokenBucket:
    '''
TokenBucket 类用于实现令牌桶算法。它有两个主要参数：MAX_CAPACITY 表示桶的最大容量，
即可以存放的令牌的最大数量；
FILL_RATE 表示每秒可以向桶中添加的令牌数量。

bucket 是一个用来存放令牌的列表。

last_fill_time 记录上一次填充令牌的时间戳。

lock 是一个用于线程同步的互斥锁。

notFull 和 notEmpty 是用于条件变量的对象，用来实现线程间的等待和通知。

TokenBucket 类的构造函数用于初始化参数和数据结构
    '''
    def __init__(self, max_capacity, fill_rate):
        
        self.MAX_CAPACITY = max_capacity
        self.FILL_RATE = fill_rate
        self.last_fill_time = time.time()
        self.bucket = []
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)
        '''
fill 方法用于向令牌桶中添加令牌。

当桶已满时，使用 not_full.wait() 让线程等待。

根据时间间隔和填充速率计算应该添加的令牌数量，并将令牌添加到 bucket 中。

not_empty.notify_all() 用于通知等待的线程，桶中有新的令牌可用。
'''
    def fill(self):
        with self.lock:
            while len(self.bucket) == self.MAX_CAPACITY:
                print("Bucket is filled now.")
                self.not_full.wait()
            now = time.time()
            num_tokens_to_add = min(self.MAX_CAPACITY - len(self.bucket), int((now - self.last_fill_time) * self.FILL_RATE))
            self.last_fill_time = now
            self.bucket.extend([random.randint(1, 100) for _ in range(num_tokens_to_add)])
            self.not_empty.notify_all()
            '''
 get 方法用于从令牌桶中获取令牌。

根据请求的令牌数量，循环从 bucket 中取出令牌，直到达到请求的数量。

当桶为空时，使用 not_empty.wait() 让线程等待。

获取令牌后，将令牌从 bucket 中移除，并通知等待的线程，桶中有空位。
            '''
    def get(self, n):
        if n <= 0:
            raise ValueError("Cannot get zero or negative number of tokens.")
        if n > self.MAX_CAPACITY:
            raise ValueError("Cannot get more tokens than max capacity.")
        result = []
        token_acquired = 0

        while token_acquired < n:
            with self.lock:
                while len(self.bucket) < 1:
                    self.not_empty.wait()
                result.append(self.bucket.pop())
                token_acquired += 1
                self.not_full.notify_all()
        return result

# Example usage:
# def fill_bucket_periodically(bucket):
#     while True:
#         time.sleep(1)
#         bucket.fill()

token_bucket = TokenBucket(max_capacity=10, fill_rate=2)
fill_thread = threading.Thread(target=token_bucket.fill)
fill_thread.daemon = True
fill_thread.start()

time.sleep(2)
tokens = token_bucket.get(5)
print("Got tokens:", tokens)
