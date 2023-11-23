class Process:

    finish_time = None
    turn_around_time = None
    waiting_time = None

    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        
        
        
processes = []
scheduler = []
memory = []
time = 0


#taking number of processes
NumberOfProcesses = int(input("Enter number of processes: "))

#taking processes info
for process in range(NumberOfProcesses):
    name = input("Enter name of process: ")
    arr = int(input("Enter arrival time: "))
    bur = int(input("Enter burst time: "))
    prio = int(input("Enter priority: "))
    
    processes.append(Process(name,arr,bur,prio))

    #sorting by arrival time
    processes = sorted(processes, key = lambda process : process.arrival_time)
 
    
bursts = []
for i in processes:
    bursts.append(i.burst_time)
    
    
#Main Logic
#adding existing processes till now
for process in processes :
    if process.arrival_time == 0 :
        memory.append(process)


#checking highest priority value
while len(memory) != 0 :
    HighestPriority = 99
    for process in memory :
        if process.priority < HighestPriority :
            HighestPriority = process.priority
    
    for i in range(len(memory)) :
        if memory[i].priority == HighestPriority :
            scheduler.append(memory[i].name)
            memory[i].burst_time = memory[i].burst_time - 1
            break
    
    
        
    #updating time
    time = time + 1
    
    #adding arrived processes
    for process in processes :
        if process.arrival_time == time :
            memory.append(process)
    
    #removing finished processes
    for item in memory[:] :
        if item.burst_time == 0 :
            item.finish_time = time
            memory.remove(item)


#Turn around time
TTAT = 0

for i in range(NumberOfProcesses) :
    processes[i].turn_around_time = processes[i].finish_time - processes[i].arrival_time

for i in processes :
    TTAT = TTAT + i.turn_around_time

average_TTAT = TTAT / NumberOfProcesses

#Waiting time
TWT = 0

for i in range(NumberOfProcesses):
    processes[i].waiting_time = processes[i].turn_around_time - bursts[i]

for i in processes :
    TWT = TWT + i.waiting_time

average_TWT = TWT / NumberOfProcesses


print("scheduler :", scheduler)
print("avgTWT = ", average_TWT )
print("avgTTAT = ", average_TTAT)

waiting_time_list = []
for i in range(NumberOfProcesses) :
    print("waiting time for p",i," = ",processes[i].waiting_time)





