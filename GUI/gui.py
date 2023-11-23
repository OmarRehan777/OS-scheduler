import tkinter as tk
from tkinter import messagebox

class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time


class SJF_NP():

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
        remaining_processes = self.processes.copy()

        while remaining_processes:
            # find the shortest job available at current time
            min_burst_time = float('inf')
            shortest_job = None
            for process in remaining_processes:
                if process.arrival_time <= current_time and process.burst_time < min_burst_time:
                    shortest_job = process
                    min_burst_time = process.burst_time

            # calculate waiting time and update current time
            waiting_time.append(current_time - shortest_job.arrival_time)
            current_time += shortest_job.burst_time

            # calculate turnaround time and update lists
            turnaround_time.append(current_time - shortest_job.arrival_time)
            # name - start time - end time
            gantt_chart.append((shortest_job.name, current_time - shortest_job.burst_time, current_time))
            burst_time.append([shortest_job.name, shortest_job.burst_time])

            # remove the processed job from the list
            remaining_processes.remove(shortest_job)


        slot_gantt_chart = []

        for i in range(len(gantt_chart)):
                for j in range(gantt_chart[i][2] - gantt_chart[i][1]):
                    slot_gantt_chart.append(gantt_chart[i][0])

        # calculate the average waiting and turnaround times
        avg_waiting_time = sum(waiting_time) / len(self.processes)
        avg_turnaround_time = sum(turnaround_time) / len(self.processes)

        return slot_gantt_chart, burst_time, avg_waiting_time, avg_turnaround_time
    counter=0
    def addButton(self):
        global scheduler
        global process_listbox
        
    # Get values from the entry widgets
        process_id = process_id_entry.get()
        burst_time = burst_time_entry.get()
        process_num= num_procs_entry.get()
        #arrival_time = arrival_time_entry.get()
        
        # Check if any entry field is empty
        if process_id == '' or burst_time == ''or process_num=='' :
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if int(process_num)<=int(SJF_NP.counter) :
            messagebox.showerror("Error", f"Number Of Processes is {process_num} only!"  )
            return
        
        

    

        # Check if the values are integers
        try:
            process_id = int(process_id)
            burst_time = int(burst_time)
            #arrival_time = int(arrival_time)
        except ValueError:
            messagebox.showerror("Error", "Process ID, Burst Time, and Arrival Time must be integers!")
            return

        # Create a new process and add it to the scheduler
        new_process = Process(process_id, SJF_NP.counter, burst_time)
        sjf_np.add_process(new_process)

        # Update the process listbox
        process_listbox.insert(tk.END, f"Process {process_id} - Arrival Time: {SJF_NP.counter}, Burst Time: {burst_time}")
        
        # Clear the entry widgets
        process_id_entry.delete(0, tk.END)
        burst_time_entry.delete(0, tk.END)
        #arrival_time_entry.delete(0, tk.END)
        SJF_NP.counter+=1
        if int(process_num)==int(SJF_NP.counter) :
            result=messagebox.askyesno("Confirmation", f"Do you want to add more processes?"  )
            result
            if result:
                 SJF_NP.counter=0
                 return
            else:
                 start()

    def runButton(self):
        
        SJF_NP.counter=0
        global sjf_np
        global remaining_burst_time_text
        global gantt_chart_canvas
        global avg_waiting_time_label
        global avg_turnaround_time_label
        
        # Run the scheduler
        gantt_chart, burst_time, avg_waiting_time, avg_turnaround_time = sjf_np.run()

        # Update the remaining burst time table
        remaining_burst_time_text.delete("1.0", tk.END)
        for process in burst_time:
            remaining_burst_time_text.insert(tk.END, f"Process {process[0]}: {process[1]}\n")

        # Update the Gantt chart
        gantt_chart_canvas.delete("all")
        slot_width = gantt_chart_canvas.winfo_width() / len(gantt_chart)
        for i, process in enumerate(gantt_chart):
            slot_x0 = i * slot_width
            slot_x1 = (i + 1) * slot_width
            slot_y0 = 0
            slot_y1 = gantt_chart_canvas.winfo_height()
            
            #gantt_chart_canvas.create_rectangle(slot_x0, slot_y0, slot_x1, slot_y1, fill=[process])
            gantt_chart_canvas.create_text((slot_x0 + slot_x1) / 2, (slot_y0 + slot_y1) / 2, text=process)
           # gantt_chart_canvas.config(width=slot_x1-slot_x0 )

        # Update the average waiting time and average turnaround time labels
        avg_waiting_time_label.config(text=f"Average Waiting Time: {avg_waiting_time:.2f}")
        avg_turnaround_time_label.config(text=f"Average Turnaround Time: {avg_turnaround_time:.2f}")
        gantt_chart_canvas.delete(tk.END)

processes=[]
sjf_np = SJF_NP()
# Create main window
root = tk.Tk()
root.title("Process Scheduler")

process_listbox_label = tk.Label(root, text="Process List")
process_listbox_label.grid(row=20)

        # Create a listbox to display the processes
process_listbox = tk.Listbox(root,width=60)
process_listbox.grid(row=21,column=1)
#process_listbox.insert(tk.END,"ID"+" " + "Burst"+" " +  "Arrival")

# Create label for scheduler type
scheduler_label = tk.Label(root, text="Scheduler Type:")
scheduler_label.grid(row=0, column=0)

# Create dropdown menu for scheduler type
scheduler_type = tk.StringVar(root)
scheduler_type.set("FCFS") # Default value
scheduler_menu = tk.OptionMenu(root, scheduler_type, "FCFS", "SJF", "Priority", "Round Robin")
scheduler_menu.grid(row=0, column=1)

# Create label for number of processes
num_procs_label = tk.Label(root, text="Number of Processes:")
num_procs_label.grid(row=1, column=0)

# Create entry widget for number of processes
num_procs_entry = tk.Entry(root)
num_procs_entry.grid(row=1, column=1)

# Create button to add process
add_button = tk.Button(root, text="Add Process")
add_button.grid(row=8, column=1, columnspan=6,padx=50)



# Create label for process ID
process_id_label = tk.Label(root, text="Process ID")
process_id_label.grid(row=3, column=0)

# Create entry widget for process ID
process_id_entry = tk.Entry(root)
process_id_entry.grid(row=3, column=1)

# Create label for burst time
burst_time_label = tk.Label(root, text="Burst Time")
burst_time_label.grid(row=4, column=0)

# Create entry widget for burst time
burst_time_entry = tk.Entry(root)
burst_time_entry.grid(row=4, column=1)

# Create label for priority (only for Priority scheduler)
priority_label = tk.Label(root, text="Priority")
priority_label.grid(row=7, column=0)

# Create entry widget for priority (only for Priority scheduler)
priority_entry = tk.Entry(root)
priority_entry.grid(row=7, column=1)

# Create button to start scheduler
start_button = tk.Button(root, text="Start Scheduler")
start_button.grid(row=8, column=0)

# Create label for remaining burst time table
remaining_burst_time_label = tk.Label(root, text="Remaining Burst Time Table:")
remaining_burst_time_label.grid(row=9, column=0)

# Create text widget for remaining burst time table
remaining_burst_time_text = tk.Text(root, height=5, width=50)
remaining_burst_time_text.grid(row=10, column=0, columnspan=3)

# Create label for Gantt chart
gantt_chart_label = tk.Label(root, text="Gantt Chart:")
gantt_chart_label.grid(row=11, column=0)

# Create canvas for Gantt chart
gantt_chart_canvas = tk.Canvas(root,width=500,height=10)
gantt_chart_canvas.grid(row=11, column=1, columnspan=3)

# Create label for average waiting time
avg_waiting_time_label = tk.Label(root, text="Average Waiting Time:")
avg_waiting_time_label.grid(row=15, column=0)

# Create label to display average waiting time
#avg_waiting_time_display = tk.Text(root,width=60,height=1)
#avg_waiting_time_display.grid(row=15, column=1)

# Create label for average turnaround time
avg_turnaround_time_label= tk.Label(root, text="Average Turnaround Time:")
avg_turnaround_time_label.grid(row=16, column=0)

#Create label to display average turnaround time
#avg_turnaround_time_display = tk.Text(root,width=60,height=1)
#avg_turnaround_time_display.grid(row=16, column=1)

#Create label for arrival time
time_arrival_label = tk.Label(root, text="Arrival Time")
time_arrival_label.grid(row=5, column=0)

#Create entry widget for arrival time 
time_arrival_entry = tk.Entry(root)
time_arrival_entry.grid(row=5, column=1)

#Create label for time quantum (only for Round Robin scheduler)
time_quantum_label = tk.Label(root, text="Time Quantum")
time_quantum_label.grid(row=6, column=0)
#Create entry widget for time quantum (only for Round Robin scheduler)
time_quantum_entry = tk.Entry(root)
time_quantum_entry.grid(row=6, column=1)

#Buttons methods
def add():
    if scheduler_type.get() == "SJF":
        SJF_NP.addButton(self=SJF_NP)
    #elif scheduler_type.get() == "FCFS":
        # Run FCFS scheduler code
    #elif scheduler_type.get() == "Priority":
        # Run Priority scheduler code
    #elif scheduler_type.get() == "Round Robin":
        # Run Round Robin scheduler code
add_button.config(command=add)    

def start():
    if scheduler_type.get() == "SJF":
        SJF_NP.runButton(self=SJF_NP)
    #elif scheduler_type.get() == "FCFS":
        # Run FCFS scheduler code
    #elif scheduler_type.get() == "Priority":
        # Run Priority scheduler code
    #elif scheduler_type.get() == "Round Robin":
        # Run Round Robin scheduler code
start_button.config(command=start)



root.mainloop()




