from Process import Process


# Find the process with the shortest remaining time at a given time
def find_shortest(proc, current_time, remaining_time):
    proc_num = len(proc)
    min_time = 9999   #set min_time to arbitrarily large value
    index = -1  

    #determine which of the processes are eligible              
    for i in range(proc_num):
        if proc[i].arrival_time <= current_time and remaining_time[i] > 0 and remaining_time[i] < min_time:
            min_time = remaining_time[i]
            index = i
    return index

#Run through Shortest Job Remaining First algorithm
def sjrf(proc):
    proc.sort(key=lambda p: p.arrival_time) #sort by arrival time
    proc_num = len(proc)
    
    completed_processes = []
    current_time = 0
    remaining_time = [p.burst_time for p in proc]

    while len(completed_processes) != proc_num:
        i = find_shortest(proc, current_time, remaining_time)  
        #keep track of time elapsed during execution of processes
        if i == -1:         #elapse time if there is not a new shortest process 
            current_time += 1
            continue
        remaining_time[i] -= 1   #reduce the total amount of remaining time after each time unit
        current_time += 1       #increase time elapsed

        #Calculate all values for each process 
        if remaining_time[i] == 0:
            current_process = proc[i]
            
            current_process.completion_time = current_time
            current_process.start_time = current_process.completion_time - current_process.burst_time            #Start = Completion - Burst
            current_process.turn_around_time = current_process.completion_time - current_process.arrival_time    #Turnaround = Completion - Arrival
            current_process.waiting_time = (current_process.turn_around_time) - current_process.burst_time       #Waiting = Turnaround - Burst
            completed_processes.append(current_process)       #keeps track of number processes completed


    return completed_processes
if __name__ == "__main__":

    #test input
    proc = [
        Process(pid=1, arrival_time=0, burst_time=8, priority=2),
        Process(pid=2, arrival_time=1, burst_time=4, priority=1),
        Process(pid=3, arrival_time=2, burst_time=9, priority=3),
        Process(pid=4, arrival_time=3, burst_time=5, priority=2),
    ]
    

    
    
    processes = sjrf(proc)
    print()
    print("Shortest Job First (Preemptive)")
    print(f"{'PID':<8}{'Arrival':<8}{'Burst':<8}{'Start':<8}{'Completion':<12}{'Turnaround':<12}{'Waiting':<8}")
    for p in processes:
        print(f"{p.pid:<8}{p.arrival_time:<8}{p.burst_time:<8}{p.start_time:<8}{p.completion_time:<12}{p.turn_around_time:<12}{p.waiting_time:<8}")