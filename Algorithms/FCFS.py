from Process import Process  

# First-Come First-Serve (FCFS) scheduling algorithm
def fcfs(processes):
    # Sort processes by arrival time/ early goes first
    processes.sort(key=lambda p: p.arrival_time)
    
    current_time = 0  # Tracks current time in the simulation
    completed_processes = []  # Stores finished processes

    for p in processes:
        # If the process arrives after current time, wait until it arrives
        p.start_time = max(current_time, p.arrival_time)
        
        # Completion time = start time + how long it runs
        p.completion_time = p.start_time + p.burst_time
        
        # Turnaround = time from arrival to complete
        p.turn_around_time = p.completion_time - p.arrival_time
        
        # Waiting = turnaround time/ how long it ran
        p.waiting_time = p.turn_around_time - p.burst_time
        
        # Move current time forward to the end of this process
        current_time = p.completion_time
        
        # Add the finished process to the list
        completed_processes.append(p)

    return completed_processes
