print("scheduler :", scheduler)
print("avgTWT = ", average_TWT )
print("avgTTAT = ", average_TTAT)

for i in range(len(processes)) :
    print("waiting time for p",i," = ",processes[i].waiting_time)