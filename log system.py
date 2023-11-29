# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 17:46:59 2023

@author: Yang Cairong
"""

import time

class Log:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        time.strftime
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        self.entries.append((timestamp, entry))

    def get_all_entries(self):
        return self.entries

# Example usage of the Log class
log = Log()

log.add_entry("Entry 1")
log.add_entry("Entry 2")
log.add_entry("Entry 3")

all_entries = log.get_all_entries()
for timestamp, entry in all_entries:
    print(f"{timestamp}: {entry}")
