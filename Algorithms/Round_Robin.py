from collections import deque

from Process import Process


def round_robin(processes, quantum):
    queue = deque()
    # track the arrival time and total quantum time
    time_taken = 0
    #sort the processes by arrival time in ascending order
    sorted(processes, key = lambda process: process.arrival_time)

    arrival_idx = 0
    #check if there is process still have not arrival yet or if there is process still need to run
    while arrival_idx < len(processes) or len(queue) > 0:
        #check if any process arrive yet
        while arrival_idx < len(processes) and time_taken >= processes[arrival_idx].arrival_time:
            queue.append(processes[arrival_idx])
            arrival_idx += 1
        if len(queue) > 0:
            top_process = queue.popleft()
            exec_time = min(quantum, top_process.remain_time)
            top_process.execution_slices.append((time_taken, exec_time))  # Record the time slice
            top_process.remain_time -= exec_time
            time_taken += exec_time
            # check again if any process arrive yet
            while arrival_idx < len(processes) and time_taken >= processes[arrival_idx].arrival_time:
                queue.append(processes[arrival_idx])
                arrival_idx += 1

            if top_process.remain_time > 0:
                queue.append(top_process)
            else:
                #Turnaround Time = Completion Time - Arrival Time
                #Waiting Time = Turnaround Time - Burst Time
                top_process.completion_time = time_taken
                top_process.turn_around_time = top_process.completion_time - top_process.arrival_time
                top_process.waiting_time = top_process.turn_around_time - top_process.burst_time
        else:
            time_taken = processes[arrival_idx].arrival_time

    return processes










