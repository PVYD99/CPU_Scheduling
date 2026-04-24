import matplotlib.pyplot as plt
import copy
# (名稱, 優先順序 ,執行時間, 顏色)
processes = [
    ["P1", 2, 10,"#81bfeb"],
    ["P2", 4, 5, "#e0b862"],
    ["P3", 1, 19,"#76da76"],
    ["P4", 5, 2, "#f47e7e"],
    ["P5", 3, 8, "#c18ff0"]
]

def draw(list):
    start = 0
    x_ticks = [0, ]

    fig, ax = plt.subplots()
    for process, y, duration, c in list[0]:
        ax.barh(0, duration, left=start, edgecolor='black', color=c)
        ax.text(start + duration / 2, 0, process, ha='center', va='center', fontsize=17, color='black', fontweight = 'roman')
        start += duration
        x_ticks.append(start)

    ax.set_xticks(x_ticks)
    ax.set_xticklabels(
        labels=x_ticks,
        fontsize=16,
        fontweight='medium'
    )
    ax.set_xlim(0, start)
    ax.set_yticks([])
    ax.set_xlabel("Time")
    ax.set_title(list[1],fontdict = {'fontsize':18,'fontweight': 'demi'})

    plt.show()

def draw_multiple(l0,l1,l2,l3):

    fig, ax = plt.subplots(4)
    i = 0
    
    for ll in l0,l1,l2,l3:
        start = 0
        x_ticks = [0, ]
        for process, y, duration, c in ll[0]:

            ax[i].barh(0, duration, left=start, edgecolor='black', color=c)
            ax[i].text(start + duration / 2, 0,process, ha='center', va='center', fontsize=17, color='black', fontweight = 'roman')
            start += duration
            x_ticks.append(start)
        ax[i].set_yticks([])
        ax[i].set_ylabel(ll[1],rotation = 0,labelpad =120,fontdict = {'fontsize':18,'fontweight': 'demi'})
        ax[i].set_xticks(x_ticks)
        ax[i].set_xticklabels(
            labels=x_ticks,
            fontsize=16,
            fontweight='medium'
            )
        ax[i].set_xlim(0, start)
        i +=1

    #plt.suptitle("CPU Scheduling Gantt Chart",fontsize=22,fontweight= 'demi')
    ax[0].set_title("CPU Scheduling Gantt Chart",fontdict = {'fontsize':18,'fontweight': 'demi'})
    ax[3].set_xlabel("Time",fontdict = {'fontsize':15,'fontweight': 'demi'})

    plt.show()


def FCFS(processes):
    title =  "FCFS( a.w.t = " + str( ( sum( processes[s][2]*(4-s) for s in range(len(processes)) ) )/len(processes)) + ")"
    return processes, title
    

def SJF(processes):
    
    sort = sorted(processes, key = lambda x : x[2])
    title =  "SJF( a.w.t = " + str( ( sum( sort[s][2]*(4-s) for s in range(len(sort)) ) )/len(processes)) + ")"
    return sort, title
    

def PS(processes):
    sort = sorted(processes, key = lambda x : x[1])
    
    title =  "PS( a.w.t = " + str( ( sum( sort[s][2]*(4-s) for s in range(len(sort)) ) )/len(processes)) + ")"
    return sort, title
    

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
                
    title =  "RR( a.w.t = " + str(awt/len(processes)) + ")"
    
    return sort, title



    


draw_multiple(FCFS(processes),SJF(processes),PS(processes),RR(processes,5))
