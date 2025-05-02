from Process import Process

def shortest_job_first(processes):
    # Sort processes by arrival time, then by burst time
    processes.sort(key=lambda p: (p.arrival_time, p.burst_time))
    
    current_time = 0
    completed_processes = []

    while processes:
        # Filter processes that have arrived
        available_processes = [p for p in processes if p.arrival_time <= current_time]
        
        if available_processes:
            # Select the process with the shortest burst time
            shortest_process = min(available_processes, key=lambda p: p.burst_time)
            processes.remove(shortest_process)
            
            # Update process times
            shortest_process.start_time = current_time
            shortest_process.completion_time = current_time + shortest_process.burst_time
            shortest_process.turn_around_time = shortest_process.completion_time - shortest_process.arrival_time
            shortest_process.waiting_time = shortest_process.turn_around_time - shortest_process.burst_time
            
            # Update current time
            current_time = shortest_process.completion_time
            
            # Add to completed processes
            completed_processes.append(shortest_process)
        else:
            # If no process is available, increment time
            current_time += 1

    return completed_processes

# Example usage
