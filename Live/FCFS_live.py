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
            burst_time.append([process.name, process.burst_time])

        slot_gantt_chart = []

        for i in range(len(gantt_chart)):
                for j in range(gantt_chart[i][2] - gantt_chart[i][1]):
                    slot_gantt_chart.append(gantt_chart[i][0])

        # calculate the average waiting and turnaround times
        avg_waiting_time = sum(waiting_time) / len(self.processes)
        avg_turnaround_time = sum(turnaround_time) / len(self.processes)

        return slot_gantt_chart, burst_time, avg_waiting_time, avg_turnaround_time



addProcess = "no"
processes = []
counter = 0
j = 0
# Create the FCFS scheduler
scheduler = FCFS()

while True:
    addProcess = input("do you want to add process? ")

    if addProcess.lower() == "close":
        break

    if addProcess.lower() == "yes":
        limit = int(input("enter number of processes: "))
        for i in range(limit):
            name = input("enter name of the process: ")
            bur = int(input("enter burst time: ")) 
            processes.append(Process(name, counter, bur))


        # Add the processes to the scheduler
        for process in processes:
            scheduler.add_process(process)

        # Run the scheduler
        gantt_chart, burst_time, avg_waiting_time, avg_turnaround_time = scheduler.run()

    counter += 1

    if j >= len(gantt_chart):
        break
    else:
        # Print the results

        # print gantt chart live
        print(gantt_chart[j])

        # print burst time table live
        for i in range(len(burst_time)):
            if burst_time[i][0] == gantt_chart[j]:
                burst_time[i][1] = burst_time[i][1] - 1    
        
        print(burst_time)

    j += 1



print("Average Waiting Time:", avg_waiting_time)
print("Average Turnaround Time:", avg_turnaround_time)

