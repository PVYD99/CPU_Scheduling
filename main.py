import matplotlib.pyplot as plt
import copy
# (名稱, 優先順序 ,執行時間)
processes = [
    ["P1", 2, 10,"#81bfeb"],
    ["P2", 4, 5, "#e0b862"],
    ["P3", 1, 19,"#76da76"],
    ["P4", 5, 2, "#f47e7e"],
    ["P5", 3, 8, "#c18ff0"]
]

def draw(list,title):
    start = 0
    x_ticks = [0,]
    
    fig, ax = plt.subplots()
    for process, y ,duration,c in list:

        ax.barh(0,duration, left = start, edgecolor='black',color = c)
        ax.text(start +duration/2, 0, process,ha='center', va='center', fontsize=14, color='black')
        start += duration
        x_ticks.append(start)
        
    ax.set_xticks(x_ticks)
    ax.set_xlim(0, start)
    ax.set_yticks([])
    ax.set_xlabel("Time")
    ax.set_title(title)

    plt.show()


def FCFS(processes):
    title =  "FCFS Gantt Chart ( a.w.t = " + str( ( sum( processes[s][2]*(4-s) for s in range(len(processes)) ) )/len(processes)) + ")"
    draw(processes, title)
    

def SJF(processes):
    
    sort = sorted(processes, key = lambda x : x[2])
    title =  "SJF Gantt Chart ( a.w.t = " + str( ( sum( sort[s][2]*(4-s) for s in range(len(sort)) ) )/len(processes)) + ")"
    draw(sort, title)
    

def PS(processes):
    sort = sorted(processes, key = lambda x : x[1])
    
    title =  "PS Gantt Chart ( a.w.t = " + str( ( sum( sort[s][2]*(4-s) for s in range(len(sort)) ) )/len(processes)) + ")"
    draw(sort, title)
    

def RR(processes, TQ):
    sort = []
    total = sum(p[2] for p in processes)
    srr = copy.deepcopy(processes)
    
    
    i = len(processes)-1
    awt = 0
    
    while(total > 0):
        
        for a in range(len(srr)):
            if srr[a][2] -TQ ==  0 :
                sort.append([srr[a][0],0,TQ,srr[a][3]])
                
                total -= TQ
                awt += srr[a][2]*i
                i-=1
                srr[a][2] -= TQ
                
            elif srr[a][2] == 0 :
                pass
            
            elif srr[a][2] - TQ < 0 :
                sort.append([srr[a][0],0 ,srr[a][2],srr[a][3]])
                total -= srr[a][2]
                
                awt += srr[a][2]*i
                i-=1
                srr[a][2] = 0
                
                


            elif srr[a][2] - TQ >= 0 :
                sort.append([srr[a][0],0,TQ,srr[a][3]])
                total -= TQ
                awt += TQ*i
                srr[a][2] -= TQ
                
    title =  "PS Gantt Chart ( a.w.t = " + str(awt/len(processes)) + ")"
    
    draw(sort, title)



    


FCFS(processes)
