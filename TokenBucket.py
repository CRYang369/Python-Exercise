import time
import threading
import random
from threading import Lock, Condition

class TokenBucket:
    def __init__(self, max_capacity, fill_rate):
        self.MAX_CAPACITY = max_capacity
        self.FILL_RATE = fill_rate
        self.last_fill_time = time.time()
        self.bucket = []
        self.lock = Lock()
        self.not_full = Condition(self.lock)
        self.not_empty = Condition(self.lock)

    def fill(self):
        with self.lock:
            while len(self.bucket) == self.MAX_CAPACITY:
                print("Bucket is filled now.")
                self.not_full.wait()
            now = time.time()
            num_tokens_to_add = min(
                self.MAX_CAPACITY - len(self.bucket),
                int((now - self.last_fill_time) / 1) * self.FILL_RATE
            )
            self.last_fill_time = now

            for _ in range(num_tokens_to_add):
                self.bucket.append(random.randint(1, 100))
            self.not_empty.notify_all()

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

# Test cases
def test_token_bucket():
    token_bucket = TokenBucket(max_capacity=10, fill_rate=2)

    def producer():
        for _ in range(5):
            time.sleep(random.uniform(0.1, 0.5))
            token_bucket.fill()

    def consumer(consumer_id):
        try:
            tokens = token_bucket.get(3)
            print(f"Consumer {consumer_id} acquired tokens: {tokens}")
        except ValueError as e:
            print(f"Consumer {consumer_id} error: {e}")

    producers = [threading.Thread(target=producer) for _ in range(2)]
    consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(5)]

    for thread in producers + consumers:
        thread.start()

    for thread in producers + consumers:
        thread.join()

if __name__ == "__main__":
    test_token_bucket()
