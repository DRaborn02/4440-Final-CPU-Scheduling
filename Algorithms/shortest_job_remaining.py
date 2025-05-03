from Process import Process

# Find the process with the shortest remaining time at a given time
def find_shortest(proc, current_time, remaining_time):
    proc_num = len(proc)
    min_time = float('inf')  # Set min_time to a very large value
    index = -1  

    # Determine which of the processes are eligible              
    for i in range(proc_num):
        if proc[i].arrival_time <= current_time and remaining_time[i] > 0 and remaining_time[i] < min_time:
            min_time = remaining_time[i]
            index = i
    return index

# Run through Shortest Job Remaining First algorithm
def sjrf(proc):
    proc.sort(key=lambda p: p.arrival_time)  # Sort by arrival time
    proc_num = len(proc)
    
    completed_processes = []
    current_time = 0
    remaining_time = [p.burst_time for p in proc]
    execution_slices = {p.pid: [] for p in proc}  # Track execution slices for each process

    while len(completed_processes) != proc_num:
        i = find_shortest(proc, current_time, remaining_time)  
        
        # Keep track of time elapsed during execution of processes
        if i == -1:  # Elapse time if there is no eligible process
            current_time += 1
            continue

        # Check if the current process is already running
        if execution_slices[proc[i].pid] and execution_slices[proc[i].pid][-1][0] + execution_slices[proc[i].pid][-1][1] == current_time:
            # Extend the current slice if the process is already running
            execution_slices[proc[i].pid][-1] = (
                execution_slices[proc[i].pid][-1][0],  # Start time remains the same
                execution_slices[proc[i].pid][-1][1] + 1  # Extend the duration
            )
        else:
            # Start a new slice if the process is not already running
            execution_slices[proc[i].pid].append((current_time, 1))

        # Reduce the remaining time of the selected process
        remaining_time[i] -= 1
        current_time += 1  # Increase the current time

        # Calculate all values for the process if it finishes
        if remaining_time[i] == 0:
            current_process = proc[i]
            current_process.completion_time = current_time
            current_process.turn_around_time = current_process.completion_time - current_process.arrival_time  # Turnaround = Completion - Arrival
            current_process.waiting_time = current_process.turn_around_time - current_process.burst_time  # Waiting = Turnaround - Burst
            completed_processes.append(current_process)  # Keep track of completed processes

    # Assign execution slices to each process
    for process in proc:
        process.execution_slices = execution_slices[process.pid]

    return proc