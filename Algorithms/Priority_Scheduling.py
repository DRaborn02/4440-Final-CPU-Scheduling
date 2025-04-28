from Process import Process

def priority_scheduling(processes):
    # Sort processes by arrival time, then by priority (lower number = higher priority)
    processes.sort(key=lambda p: (p.arrival_time, p.priority))
    
    current_time = 0
    completed_processes = []

    while processes:
        # Get processes that have arrived and are ready to execute
        ready_queue = [p for p in processes if p.arrival_time <= current_time]
        
        if ready_queue:
            # Select the process with the highest priority (lowest priority number)
            ready_queue.sort(key=lambda p: p.priority)
            current_process = ready_queue[0]
            
            # Simulate process execution
            current_process.start_time = current_time
            current_process.completion_time = current_time + current_process.burst_time
            current_process.turn_around_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turn_around_time - current_process.burst_time
            
            # Update current time
            current_time = current_process.completion_time
            
            # Add the completed process to the completed list and remove it from the queue
            completed_processes.append(current_process)
            processes.remove(current_process)
        else:
            # If no process is ready, increment the current time
            current_time += 1

    return completed_processes
