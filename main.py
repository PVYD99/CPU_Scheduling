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

def FCFS(processes):
    x_ticks = [0,]
    fig, ax = plt.subplots()
    start = 0

    for process, y ,duration in processes:

        ax.barh(0,duration, left = start, edgecolor='black')
        ax.text(start +duration/2, 0, process,ha='center', va='center', fontsize=14, color='black')
        start += duration
        x_ticks.append(start)

    ax.set_xticks(x_ticks)
    ax.set_xlim(0, start)
    ax.set_yticks([])
    ax.set_xlabel("Time")
    ax.set_title("FCFS Gantt Chart")

    plt.show()

def SJF(processes):
    x_ticks = [0,]
    fig, ax = plt.subplots()
    start = 0
    sort = sorted(processes, key = lambda x : x[2])
    for process, y ,duration in sort:

        ax.barh(0,duration, left = start, edgecolor='black')
        ax.text(start +duration/2, 0, process,ha='center', va='center', fontsize=14, color='black')
        start += duration
        x_ticks.append(start)

    ax.set_xticks(x_ticks)
    ax.set_xlim(0, start)
    ax.set_yticks([])
    ax.set_xlabel("Time")
    ax.set_title("SJF Gantt Chart")

    plt.show()

def PS(processes):
    x_ticks = [0,]
    fig, ax = plt.subplots()
    start = 0
    sort = sorted(processes, key = lambda x : x[1])
    for process, y ,duration in sort:

        ax.barh(0,duration, left = start, edgecolor='black')
        ax.text(start +duration/2, 0, process,ha='center', va='center', fontsize=14, color='black')
        start += duration
        x_ticks.append(start)

    ax.set_xticks(x_ticks)
    ax.set_xlim(0, start)
    ax.set_yticks([])
    ax.set_xlabel("Time")
    ax.set_title("PS Gantt Chart")

    plt.show()

def RR(processes, TQ):
    fig, ax = plt.subplots()
    start = 0
    sort = []
    total = sum(p[2] for p in processes)

    srr = copy.deepcopy(processes)
    x_ticks = [0,]
    while(total > 0):

        for a in range(len(srr)):

            if srr[a][2] == 0 :
                pass
            elif srr[a][2] - TQ < 0 :
                sort.append([srr[a][0], srr[a][2]])
                total -= srr[a][2]
                srr[a][2] = 0


            elif srr[a][2] - TQ >= 0 :
                sort.append([srr[a][0], TQ])
                srr[a][2] -= TQ
                total -= TQ
            print("total:" , total , "    ",srr)


    for process, duration in sort:

        ax.barh(0,duration, left = start, edgecolor='black')
        ax.text(start +duration/2, 0, process,ha='center', va='center', fontsize=14, color='black')
        start += duration
        x_ticks.append(start)

    ax.set_xticks(x_ticks)

    ax.set_xlim(0, start)
    ax.set_yticks([])
    ax.set_xlabel("Time")
    ax.set_title("RR Gantt Chart")



    plt.show()


RR(processes, 5)