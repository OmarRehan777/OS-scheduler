class Process:

    finish_time = 0
    turn_around_time = 0
    waiting_time = 0

    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        


#initializing
time = 0
processes = []
scheduler = []
memory = []
bursts = []



while len(memory) != 0 or time == 0 :
    AddProcess = input("Want to add new processes ? ").lower()

    if AddProcess == "yes" :
        no_of_added_processes = int(input("Enter number of processes : "))
        
        for i in range(no_of_added_processes):
            name = input("Enter name of process: ")
            bur = int(input("Enter burst time: "))
            prio = int(input("Enter priority: "))
            arr = time
            
            processes.append(Process(name,arr,bur,prio))
            memory.append(Process(name,arr,bur,prio))

            bursts.append(bur)
            
            #sorting by arrival time
            processes = sorted(processes, key = lambda process : process.arrival_time)
            memory = sorted(memory, key = lambda process : process.arrival_time)        
   
            
            
    #checking highest priority value
    while len(memory) != 0 :
        HighestPriority = 99
        for process in memory :
            if process.priority < HighestPriority :
                HighestPriority = process.priority

    #adding process with highest priority to scheduler
        for i in range(len(memory)) :
            if memory[i].priority == HighestPriority :
                scheduler.append(memory[i].name)
                memory[i].burst_time = memory[i].burst_time - 1
                break
            
        #MAIN PRINT
        print(scheduler[-1])
        
        live_bursts = [(memory[i].name ,memory[i].burst_time) for i in range(len(memory))]
        print(live_bursts)
        
        #removing finished processes
        for item in memory[:] :
            if item.burst_time == 0 :
                for x in range(len(processes)):
                    if processes[x].name == item.name:
                        processes[x].finish_time = time + 1
                memory.remove(item)
                


        #updating time
        time = time + 1
        
        break

    


#Turn around time
TTAT = 0

for i in range(len(processes)) :
    processes[i].turn_around_time = processes[i].finish_time - processes[i].arrival_time

for i in processes :
    TTAT = TTAT + i.turn_around_time

average_TTAT = TTAT / len(processes)




#Waiting time
TWT = 0

for i in range(len(processes)):
    processes[i].waiting_time = processes[i].turn_around_time - bursts[i]

for i in processes :
    TWT = TWT + i.waiting_time

average_TWT = TWT / len(processes)


    
print("scheduler :", scheduler)
print([(processes[i].name, processes[i].finish_time, processes[i].arrival_time) for i in range(len(processes))])
print([(processes[i].name, processes[i].turn_around_time, bursts[i]) for i in range(len(processes))])
print("avgTWT = ", average_TWT )
print("avgTTAT = ", average_TTAT)

