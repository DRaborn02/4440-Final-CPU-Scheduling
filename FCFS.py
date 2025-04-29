from Process import Process  # Import the Process class 

# First-Come First-Serve (FCFS) scheduling algorithm
def fcfs(processes):
    # Sort processes by arrival time (earliest process first)
    processes.sort(key=lambda p: p.arrival_time)
    
    current_time = 0  # Tracks current time in the simulation
    completed_processes = []  # Stores finished processes

    for p in processes:
        # If the process arrives after current time, wait until it arrives
        p.start_time = max(current_time, p.arrival_time)
        
        # Completion time = start time + how long it runs
        p.completion_time = p.start_time + p.burst_time
        
        # Turnaround = time from arrival to completion
        p.turn_around_time = p.completion_time - p.arrival_time
        
        # Waiting = turnaround time - how long it ran
        p.waiting_time = p.turn_around_time - p.burst_time
        
        # Move current time forward to the end of this process
        current_time = p.completion_time
        
        # Add the finished process to the list
        completed_processes.append(p)

    return completed_processes

# Example test run of FCFS
if __name__ == "__main__":
    # Create example list of processes (same as your teammates are using)
    processes = [
        Process(pid=1, arrival_time=0, burst_time=8, priority=2),
        Process(pid=2, arrival_time=1, burst_time=4, priority=1),
        Process(pid=3, arrival_time=2, burst_time=9, priority=3),
        Process(pid=4, arrival_time=3, burst_time=5, priority=2),
    ]

    # Run FCFS algorithm on the list
    completed = fcfs(processes)

    # Print the results in table format
    print("\nFirst-Come, First-Serve Scheduling")
    print(f"{'PID':<8}{'Arrival':<8}{'Burst':<8}{'Start':<8}{'Completion':<12}{'Turnaround':<12}{'Waiting':<8}")
    for p in completed:
        print(f"{p.pid:<8}{p.arrival_time:<8}{p.burst_time:<8}{p.start_time:<8}{p.completion_time:<12}{p.turn_around_time:<12}{p.waiting_time:<8}")
