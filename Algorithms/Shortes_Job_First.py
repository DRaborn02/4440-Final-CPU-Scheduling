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
if __name__ == "__main__":
    # Create a list of Process instances
    process_list = [
        Process(pid=1, arrival_time=0, burst_time=8, priority=2),
        Process(pid=2, arrival_time=1, burst_time=4, priority=1),
        Process(pid=3, arrival_time=2, burst_time=9, priority=3),
        Process(pid=4, arrival_time=3, burst_time=5, priority=2),
    ]

    # Run SJF scheduling
    completed = shortest_job_first(process_list)

    # Print results
   # Print results with proper alignment
print(f"{'PID':<8}{'Arrival':<8}{'Burst':<8}{'Start':<8}{'Completion':<12}{'Turnaround':<12}{'Waiting':<8}")
for p in completed:
    print(f"{p.pid:<8}{p.arrival_time:<8}{p.burst_time:<8}{p.start_time:<8}{p.completion_time:<12}{p.turn_around_time:<12}{p.waiting_time:<8}")