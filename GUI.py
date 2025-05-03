import tkinter as tk
from tkinter import ttk
from Process import Process

from Algorithms.Priority_Scheduling import priority_scheduling
from Algorithms.Shortes_Job_First import shortest_job_first
from Algorithms.FCFS import fcfs
from Algorithms.shortest_job_remaining import sjrf
from Algorithms.Round_Robin import round_robin

# Create the main application window
root = tk.Tk()
root.title("Process Input")
root.minsize(width=575, height=400)
root.maxsize(width=575, height=1000)

# Configure the root window to allow dynamic resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a frame to hold the canvas and scrollbar
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, sticky="nsew")

# Create a canvas for scrolling
canvas = tk.Canvas(main_frame)
canvas.grid(row=0, column=0, sticky="nsew")

# Add a vertical scrollbar to the canvas
scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

# Configure the canvas to work with the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the process rows
process_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=process_frame, anchor="nw")

# Configure the main frame to allow dynamic resizing
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Function to update the scroll region dynamically
def update_scroll_region(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Bind the resizing event to update the scroll region
process_frame.bind("<Configure>", update_scroll_region)

# Create a header row
tk.Label(process_frame, text="Process Number").grid(row=0, column=0, padx=10, pady=5)
tk.Label(process_frame, text="Arrival Time").grid(row=0, column=1, padx=10, pady=5)
tk.Label(process_frame, text="Burst Time").grid(row=0, column=2, padx=10, pady=5)
tk.Label(process_frame, text="Priority").grid(row=0, column=3, padx=10, pady=5)

# List to keep track of process rows
process_rows = []

# Function to add a new process row
def add_process():
    row = len(process_rows) + 1
    process_number_label = tk.Label(process_frame, text=str(row))
    process_number_label.grid(row=row, column=0, padx=10, pady=5)
    
    arrival_time_entry = ttk.Entry(process_frame)
    arrival_time_entry.grid(row=row, column=1, padx=10, pady=5)
    
    burst_time_entry = ttk.Entry(process_frame)
    burst_time_entry.grid(row=row, column=2, padx=10, pady=5)
    
    priority_entry = ttk.Entry(process_frame)
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
    
    # Get the quantum value from the entry box
    try:
        quantum = int(quantum_entry.get())
    except ValueError:
        print("Invalid input for Time Quantum. Please enter a valid integer.")
        return

    # Run and display results for each algorithm
    algorithms = {
        "Priority Scheduling": priority_scheduling,
        "Shortest Job First (SJF)": shortest_job_first,
        "First Come First Serve (FCFS)": fcfs,
        "Shortest Job Remaining (SJF-Preemptive)": sjrf,
        "Round Robin": lambda processes: round_robin(processes, quantum)  # Pass quantum to Round Robin
    }

    for name, algorithm in algorithms.items():
        # Make a copy of the processes for each algorithm
        algorithm_processes = [Process(p.pid, p.arrival_time, p.burst_time, p.priority) for p in processes]
        completed_processes = algorithm(algorithm_processes)
        
        # Display the results in the console
        print(f"\n{name} Results:")
        print("PID\tArrival\tBurst\tPriority\tStart\tCompletion\tTAT\tWaiting")
        for p in completed_processes:
            print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.priority}\t\t{p.start_time}\t{p.completion_time}\t\t{p.turn_around_time}\t{p.waiting_time}")


# Add buttons and quantum input below the scrollable section
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Add buttons to add, remove, and submit processes inside the button_frame
add_button = ttk.Button(button_frame, text="Add Process", command=add_process)
add_button.grid(row=0, column=0, padx=10, pady=5)

remove_button = ttk.Button(button_frame, text="Remove Process", command=remove_process)
remove_button.grid(row=0, column=1, padx=10, pady=5)

submit_button = ttk.Button(button_frame, text="Submit", command=submit_process)
submit_button.grid(row=0, column=2, padx=10, pady=5)

# Add a frame for the quantum label and entry box inside the button_frame
quantum_frame = tk.Frame(button_frame)
quantum_frame.grid(row=0, column=3, padx=10, pady=5, sticky="e")

# Add a label and entry box for the time quantum inside the quantum_frame
quantum_label = tk.Label(quantum_frame, text="Time Quantum:")
quantum_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

quantum_entry = ttk.Entry(quantum_frame, width=10)
quantum_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Add the first process row by default
add_process()

# Run the application
root.mainloop()