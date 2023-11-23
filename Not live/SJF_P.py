class Process:
    def _init_(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time


class SJF_P():
    def _init_(self):
        super()._init_()
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def run(self):
        self.processes.sort(key=lambda p: p.arrival_time)

        gantt_chart = []  # initialize the Gantt chart
        burst_time = []
        waiting_time = []
        turnaround_time = []
        current_time = 0
        remaining_processes = self.processes.copy()

        while remaining_processes:
            # find the shortest job available at current time
            min_burst_time = float('inf')
            shortest_job = None
            for process in remaining_processes:
                if process.arrival_time <= current_time and process.remaining_time < min_burst_time:
                    shortest_job = process
                    min_burst_time = process.remaining_time

            # update Gantt chart
            if not gantt_chart:
                # If Gantt chart is empty, add the first process
                gantt_chart.append((shortest_job.name, current_time, current_time+1))
            elif gantt_chart[-1][0] == shortest_job.name:
                # If the last process in Gantt chart is the same as the current process, update its end time
                gantt_chart[-1] = (shortest_job.name, gantt_chart[-1][1], current_time+1)
            else:
                # If the last process in Gantt chart is different from the current process, add the current process
                gantt_chart.append((shortest_job.name, current_time, current_time+1))

            # reduce remaining time of current job and update current time
            shortest_job.remaining_time -= 1
            current_time += 1

            # add completed job to the lists
            if shortest_job.remaining_time == 0:
                burst_time.append(shortest_job.burst_time)
                waiting_time.append(current_time - shortest_job.arrival_time - shortest_job.burst_time)
                turnaround_time.append(current_time - shortest_job.arrival_time)
                remaining_processes.remove(shortest_job)

        # calculate the average waiting and turnaround times
        avg_waiting_time = sum(waiting_time) / len(self.processes)
        avg_turnaround_time = sum(turnaround_time) / len(self.processes)

        # add the end time for the last process in the Gantt chart
        gantt_chart[-1] = (gantt_chart[-1][0], gantt_chart[-1][1], current_time)

        return gantt_chart, burst_time, avg_waiting_time, avg_turnaround_time


# Get user input for processes
processes = []
limit = int(input("Enter number of processes: "))
for i in range(limit):
    name = input("Enter name of the process: ")
    arr = int(input("Enter arrival time: "))
    bur = int(input("Enter burst time: "))
    processes.append(Process(name, arr, bur))


# Create the SJF Preemptive scheduler
scheduler = SJF_P()

# Add the processes to the scheduler
for process in processes:
    scheduler.add_process(process)

# Run the scheduler
gantt_chart, burst_time, avg_waiting_time, avg_turnaround_time = scheduler.run()

# Print the results
print("Gantt Chart:")
print(gantt_chart)
print("Average Waiting Time:", avg_waiting_time)
print("Average Turnaround Time:", avg_turnaround_time)