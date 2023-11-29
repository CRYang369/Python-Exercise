# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 23:45:10 2023

@author: Yang Cairong
"""
import time
from datetime import datetime

class Employee:
    def __init__(self, name, position, hourly_rate):
        self.name = name
        self.position = position
        self.hourly_rate = hourly_rate
        self.clock_in_time = None
        self.clock_out_time = None
        self.total_hours = 0
        self.total_earnings = 0

    def clock_in(self):
        if not self.clock_in_time:  # 避免重复打卡
            self.clock_in_time = self.get_current_time()

    def clock_out(self):
        if self.clock_in_time and not self.clock_out_time:  # 只有在已打卡但未打卡出的情况下才能打卡出
            self.clock_out_time = self.get_current_time()
            self.calculate_hours()
            self.calculate_earnings()

    def calculate_hours(self):
        if self.clock_in_time and self.clock_out_time:
            time_worked = self.clock_out_time - self.clock_in_time
            self.total_hours += time_worked.total_seconds() / 3600
            self.clock_in_time = None
            self.clock_out_time = None

    def calculate_earnings(self):
        self.total_earnings += self.total_hours * self.hourly_rate

    def get_current_time(self):
        # 这里用于获取当前时间，可以替换为其他时间获取方法（如从数据库、网络等获取时间）
        return datetime.now()

# Example usage
emp1 = Employee("John", "Manager", 15.0)

emp1.clock_in()
# ... do some work ...
# time.sleep(300)
emp1.clock_out()

print(f"{emp1.name} worked for {emp1.total_hours:.2f} hours and earned ${emp1.total_earnings:.2f}.")
