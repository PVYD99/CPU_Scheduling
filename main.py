import matplotlib.pyplot as plt
import copy
# (名稱, 優先順序 ,執行時間)
processes = [
    ["P1", 2, 10],
    ["P2", 4, 5],
    ["P3", 1, 19],
    ["P4", 5, 2],
    ["P5", 3, 8]
]

def draw(list):
    start = 0
    x_ticks = [0,]
    fig, ax = plt.subplots()
    for process, y ,duration in list[0]:

        ax.barh(0,duration, left = start, edgecolor='black')
        ax.text(start +duration/2, 0, process,ha='center', va='center', fontsize=14, color='black')
        start += duration
        x_ticks.append(start)
        
    ax.set_xticks(x_ticks)
    ax.set_xlim(0, start)
    ax.set_yticks([])
    ax.set_xlabel("Time")
    ax.set_title(list[1])

    plt.show()


def FCFS(processes):
    return processes, "FCFS Gantt Chart"
    

def SJF(processes):
    
    sort = sorted(processes, key = lambda x : x[2])
    return sort, "SJF Gantt Chart"
    

def PS(processes):
    sort = sorted(processes, key = lambda x : x[1])
    return sort, "PS Gantt Chart"
    

def RR(processes, TQ):
    sort = []
    total = sum(p[2] for p in processes)
    srr = copy.deepcopy(processes)
    
    while(total > 0):

        for a in range(len(srr)):

            if srr[a][2] == 0 :
                pass
            elif srr[a][2] - TQ < 0 :
                sort.append([srr[a][0],0 ,srr[a][2]])
                total -= srr[a][2]
                srr[a][2] = 0


            elif srr[a][2] - TQ >= 0 :
                sort.append([srr[a][0],0,TQ])
                srr[a][2] -= TQ
                total -= TQ
            print("total:" , total , "    ",srr)

    
    return sort, "RR Gantt Chart"



    


draw(RR(processes, 5))
draw(FCFS(processes))
draw(SJF(processes))
draw(PS(processes))