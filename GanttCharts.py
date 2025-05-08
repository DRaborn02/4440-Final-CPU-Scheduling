import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def create_gantt_chart(algorithm_name, processes):
    """
    Create a Gantt chart for a given scheduling algorithm and its processes.
    """
    fig, ax = plt.subplots(figsize=(10, 1.5))
    colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33A8']  # Color palette for processes

    # Create Gantt chart bars
    for i, process in enumerate(processes):
        # Check if execution_slices is populated
        if process.execution_slices:
            for slice_start, slice_duration in process.execution_slices:
                ax.barh(
                    y=process.pid, 
                    width=slice_duration, 
                    left=slice_start, 
                    color=colors[i % len(colors)], 
                    edgecolor='black'
                )
                ax.text(
                    slice_start + slice_duration / 2, 
                    process.pid, 
                    f"P{process.pid}", 
                    ha='center', 
                    va='center', 
                    color='white', 
                    fontsize=10
                )
        else:
            # Fallback to using start_time and burst_time
            ax.barh(
                y=process.pid, 
                width=process.burst_time, 
                left=process.start_time, 
                color=colors[i % len(colors)], 
                edgecolor='black'
            )
            ax.text(
                process.start_time + process.burst_time / 2, 
                process.pid, 
                f"P{process.pid}", 
                ha='center', 
                va='center', 
                color='white', 
                fontsize=10
            )

    # Set labels and title
    ax.set_xlabel("Time")
    ax.set_ylabel("Processes")
    ax.set_title(f"Gantt Chart - {algorithm_name}")
    ax.set_yticks([p.pid for p in processes])
    ax.set_yticklabels([f"P{p.pid}" for p in processes])
    ax.grid(axis='x', linestyle='--', alpha=0.7)

    # Add legend
    legend_elements = [Patch(facecolor=colors[i % len(colors)], edgecolor='black', label=f"P{p.pid}") for i, p in enumerate(processes)]
    ax.legend(handles=legend_elements, title="Processes", loc='upper right')

    # Show the chart
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

def generate_all_gantt_charts(results):
    """
    Generate Gantt charts for all 5 algorithms in a single window.
    :param results: A dictionary where keys are algorithm names and values are lists of completed processes.
    """
    num_algorithms = len(results)
    fig, axes = plt.subplots(num_algorithms, 1, figsize=(10, 2.5 * num_algorithms))  # Adjusted height
    fig.suptitle("Gantt Charts for All Algorithms", fontsize=10)

    # Create a consistent color mapping for processes
    all_pids = {p.pid for processes in results.values() for p in processes}  # Collect all unique PIDs
    colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33A8', '#FF8C00', '#8A2BE2', '#00CED1']  # Extend color palette if needed
    color_map = {pid: colors[i % len(colors)] for i, pid in enumerate(sorted(all_pids))}  # Map PIDs to colors

    # If there's only one algorithm, axes won't be a list
    if num_algorithms == 1:
        axes = [axes]

    for ax, (algorithm_name, processes) in zip(axes, results.items()):
        # Calculate average waiting time
        total_waiting_time = sum(p.waiting_time for p in processes)
        avg_waiting_time = total_waiting_time / len(processes) if processes else 0

        for process in processes:
            if process.execution_slices:
                for slice_start, slice_duration in process.execution_slices:
                    ax.barh(
                        y=process.pid,
                        width=slice_duration,
                        left=slice_start,
                        color=color_map[process.pid],  # Use consistent color from the color map
                        edgecolor='black'
                    )
                    ax.text(
                        slice_start + slice_duration / 2,
                        process.pid,
                        f"P{process.pid}",
                        ha='center',
                        va='center',
                        color='black',  # Text color for better contrast
                        fontsize=8
                    )
            else:
                ax.barh(
                    y=process.pid,
                    width=process.burst_time,
                    left=process.start_time,
                    color=color_map[process.pid],  # Use consistent color from the color map
                    edgecolor='black'
                )
                ax.text(
                    process.start_time + process.burst_time / 2,
                    process.pid,
                    f"P{process.pid}",
                    ha='center',
                    va='center',
                    color='black',  # Text color for better contrast
                    fontsize=8
                )

        # Update title to include average waiting time
        ax.set_title(f"{algorithm_name} (Avg Wait Time: {avg_waiting_time:.2f})", fontsize=10)
        ax.set_ylabel("Processes", fontsize=8)
        ax.set_yticks([p.pid for p in processes])
        ax.set_yticklabels([f"P{p.pid}" for p in processes], fontsize=8)
        ax.grid(axis='x', linestyle='--', alpha=0.7)

    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout for compactness
    fig.subplots_adjust(hspace=0.6, bottom=0.04)  # Increased vertical space between subplots
    plt.show()