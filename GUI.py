import tkinter as tk
from tkinter import ttk
from Process import Process
from Algorithms.Priority_Scheduling import priority_scheduling

# Create the main application window
root = tk.Tk()
root.title("Process Input")

# Create a header row
tk.Label(root, text="Process Number").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Arrival Time").grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Burst Time").grid(row=1, column=2, padx=10, pady=5)
tk.Label(root, text="Priority").grid(row=1, column=3, padx=10, pady=5)

# List to keep track of process rows
process_rows = []

# Function to add a new process row
def add_process():
    row = len(process_rows) + 3
    process_number_label = tk.Label(root, text=str(row-2))
    process_number_label.grid(row=row, column=0, padx=10, pady=5)
    
    arrival_time_entry = ttk.Entry(root)
    arrival_time_entry.grid(row=row, column=1, padx=10, pady=5)
    
    burst_time_entry = ttk.Entry(root)
    burst_time_entry.grid(row=row, column=2, padx=10, pady=5)
    
    priority_entry = ttk.Entry(root)
    priority_entry.grid(row=row, column=3, padx=10, pady=5)
    
    process_rows.append((process_number_label, arrival_time_entry, burst_time_entry, priority_entry))

# Function to remove the last process row
def remove_process():
    if process_rows:
        process_number_label, arrival_time_entry, burst_time_entry, priority_entry = process_rows.pop()
        process_number_label.destroy()
        arrival_time_entry.destroy()
        burst_time_entry.destroy()
        priority_entry.destroy()

# Add a button to submit the data
def submit_process():
    processes = []
    for i, (process_number_label, arrival_time_entry, burst_time_entry, priority_entry) in enumerate(process_rows, start=1):
        try:
            # Collect data from the text boxes
            arrival_time = int(arrival_time_entry.get())
            burst_time = int(burst_time_entry.get())
            priority = int(priority_entry.get())
            
            # Create a Process object
            process = Process(pid=i, arrival_time=arrival_time, burst_time=burst_time, priority=priority)
            processes.append(process)
        except ValueError:
            print(f"Invalid input for Process {i}. Please enter valid integers.")
            return
        
    # Run the priority scheduling algorithm
    priority_completed_processes = priority_scheduling(processes)
    
    # Display the results in the console
    print("PID\tArrival\tBurst\tPriority\tStart\tCompletion\tTAT\tWaiting")
    for p in priority_completed_processes:
        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.priority}\t\t{p.start_time}\t{p.completion_time}\t\t{p.turn_around_time}\t{p.waiting_time}")


submit_button = ttk.Button(root, text="Submit", command=submit_process)
submit_button.grid(row=0, column=4, padx=10, pady=5)

# Add buttons to add and remove processes
add_button = ttk.Button(root, text="Add Process", command=add_process)
add_button.grid(row=0, column=0, columnspan=2, pady=10)

remove_button = ttk.Button(root, text="Remove Process", command=remove_process)
remove_button.grid(row=0, column=2, columnspan=2, pady=10)

# Add the first process row by default
add_process()

# Run the application
root.mainloop()