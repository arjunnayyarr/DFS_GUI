import Main
import GUI
import time

search = []

def DFS(v):
    print(v+1)
    GUI.FillOval(v, "yellow")
    search[v] = 1
    for i in range(0, len(Main.adjacency_matrix)):
        if(Main.adjacency_matrix[v][i] == 1 and search[i] != 1):
            print(str(v+1)+" to "+str(i+1)+" Because they are connected ")
            time.sleep(2)
            DFS(i)
