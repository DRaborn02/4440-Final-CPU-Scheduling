class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remain_time = burst_time
        self.priority = priority
        self.start_time = 0
        self.completion_time = 0
        self.turn_around_time = 0
        self.waiting_time = 0
        self.execution_slices = [] 