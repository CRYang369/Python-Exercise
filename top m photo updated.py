# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 12:27:46 2023

@author: Yang Cairong
"""

import heapq
from collections import defaultdict

class Log:
    def __init__(self, photo_id, timestamp):
        self.photo_id = photo_id
        self.timestamp = timestamp
        
    # def __lt__(self, other):
    #     return self.timestamp < other.timestamp

class LogIterator:
    def __init__(self, logs):
        # self.logs = sorted(logs)
        # self.logs = sorted(logs,key=lambda log: log.timestamp)
        self.logs=logs
        self.index = 0
        
    def has_next(self):
        return self.index < len(self.logs)
    
    def next_one(self):
        if self.has_next():
            log = self.logs[self.index]
            self.index += 1
            return log
        else:
            return None

class TopMPhotos:
    def __init__(self):
        self.photo_dict = defaultdict(list)
        self.most_visited = []

    def insert_log(self, log):
        self.photo_dict[log.photo_id].append(log)
        
    def get_top_m(self, m):
        for photo_id, logs in self.photo_dict.items():
            total_visits = len(logs)
            heapq.heappush(self.most_visited, (-total_visits, photo_id))

        result = []
        for _ in range(m):
            if self.most_visited:
                visits, photo_id = heapq.heappop(self.most_visited)
                result.append((photo_id, -visits))
        return result

# Test with the provided logs
logs = [
    {'photoId': 1, 'timestamp': '2023-08-01'},
    {'photoId': 2, 'timestamp': '2023-08-02'},
    {'photoId': 3, 'timestamp': '2023-08-02'},
    {'photoId': 3, 'timestamp': '2023-08-03'},
    {'photoId': 4, 'timestamp': '2023-08-04'},
    {'photoId': 5, 'timestamp': '2023-08-02'},
    {'photoId': 5, 'timestamp': '2023-08-10'},
    {'photoId': 6, 'timestamp': '2023-08-02'},
    {'photoId': 6, 'timestamp': '2023-08-09'},
    {'photoId': 6, 'timestamp': '2023-08-02'},
    {'photoId': 6, 'timestamp': '2023-08-04'},
    {'photoId': 4, 'timestamp': '2023-08-02'},
    {'photoId': 3, 'timestamp': '2023-08-05'},
    {'photoId': 2, 'timestamp': '2023-08-02'},
    {'photoId': 7, 'timestamp': '2023-08-06'},
]

log_objects = [Log(log['photoId'], log['timestamp']) for log in logs]
log_iterator = LogIterator(log_objects)

top_m_photos = TopMPhotos()
while log_iterator.has_next():
    log = log_iterator.next_one()
    top_m_photos.insert_log(log)

m = 4
top_m = top_m_photos.get_top_m(m)
print(top_m)
