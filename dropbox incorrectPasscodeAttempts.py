# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 23:46:50 2023

@author: Yang Cairong
"""

def solution(passcode, cur_password):
    consecutive_failures = 0
    attempts=[]

    # for attempt in attempts:
    if cur_password != passcode:
        attempts.append(cur_password)
        consecutive_failures += 1
        # if consecutive_failures
        if len(attempts) == 10:
            return True
    else:
        consecutive_failures = 0

    return False




# passcode = "1234"

# attempts = ["9999", "9999",
#             "9999", "9999",
#             "9999", "9999",
#             "9999", "1234",
#             "9999", "9999",
#             "9999", "9999"]
passcode = "1111" 

attempts = ["1111", "4444",
            "9999", "3333",
            "8888", "2222",
            "7777", "0000",
            "6666", "7285",
            "5555", "1111"]
for cur_pass in attempts:
    print(solution(passcode, cur_pass) )