class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time



class FCFS():
    def __init__(self):
        super().__init__()
        self.processes = []  # add a processes list attribute

    def add_process(self, process):
        self.processes.append(process)  # add the process to the processes list

    def run(self):
        self.processes.sort(key=lambda p: p.arrival_time)  # sort the processes based on arrival time

        gantt_chart = []  # initialize the Gantt chart
        burst_time = []  # initialize the burst time list
        waiting_time = []  # initialize the waiting time list
        turnaround_time = []  # initialize the turnaround time list
        current_time = 0  # initialize the current time to 0

        for process in self.processes:
            # calculate waiting time and update current time
            waiting_time.append(current_time - process.arrival_time)
            current_time += process.burst_time

            # calculate turnaround time and update lists
            turnaround_time.append(current_time - process.arrival_time)
            # name - start time - end time
            gantt_chart.append((process.name, current_time - process.burst_time, current_time))
            burst_time.append(process.burst_time)

        # calculate the average waiting and turnaround times
        avg_waiting_time = sum(waiting_time) / len(self.processes)
        avg_turnaround_time = sum(turnaround_time) / len(self.processes)

        return gantt_chart, burst_time, avg_waiting_time, avg_turnaround_time

    
processes = []

limit = int(input("enter number of processes: "))

for i in range(limit):
    name = input("enter name of the process: ")
    arr = int(input("enter arrival time: ")) 
    bur = int(input("enter burst time: ")) 
    processes.append(Process(name, arr, bur))



# Create the FCFS scheduler
scheduler = FCFS()

# Add the processes to the scheduler
for process in processes:
    scheduler.add_process(process)

# Run the scheduler
gantt_chart, burst_time, avg_waiting_time, avg_turnaround_time = scheduler.run()

# Print the results
print("Gantt Chart:")
print(gantt_chart)
print("Burst Time:")
print(burst_time)
print("Average Waiting Time:", avg_waiting_time)
print("Average Turnaround Time:", avg_turnaround_time)

