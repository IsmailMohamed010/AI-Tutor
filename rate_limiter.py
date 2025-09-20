import time

class RateLimiter:
    def __init__(self, min_interval=30):
        self.last_request_time = 0
        self.min_interval = min_interval

    def can_request(self):
        now = time.time()
        elapsed = now - self.last_request_time
        if elapsed < self.min_interval:
            return False, int(self.min_interval - elapsed)
        self.last_request_time = now
        return True, 0
