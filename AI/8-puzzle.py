from queue import PriorityQueue
import copy

class State:
    def __init__(self, puzzle, level=0, h=0):
        self.puzzle = puzzle
        self.level = level
        self.h = h
        self.cost = h + level

    def __lt__(self, other):
        # This defines how the heapq compares states: by cost, then by level
        if self.cost == other.cost:
            return self.level < other.level
        return self.cost < other.cost
    
gl = [[1,2,3],
        [8,0,4],
        [7,6,5]]

ini = [[2,8,3],
            [1,6,4],
            [7,0,5]]

def fScore(curr , goal):
    count = 0
    for i in range(len(curr)):
        for j in range(len(curr[i])):
            if curr[i][j] != goal[i][j]:
                count = count + 1
    return count

def calScore(temp:State ,goal):
    c = fScore(temp.puzzle , goal)
    temp.level = temp.level +1
    if c ==0:
        temp.cost = 0
    else :
        temp.cost = temp.level + c
        
    return temp

def getZero(temp):
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == 0:
                return i,j
    return 0,0


def display(temp):
    for i in range(len(temp.puzzle)):
        for j in range(len(temp.puzzle)):
            print(temp.puzzle[i][j],end=" ")
        print()
    print()
    print(f" h : {temp.h}")
    print(f" level : {temp.level}")
    print(f" cost : {temp.cost} \n")

def solve(ini , gl):
    h = fScore(ini , gl)
    starter = State(ini , 0 ,h  )
    pq = PriorityQueue()
    # heap.heappush(pq, starter)
    pq.put(starter)
    
    vis = []
    while pq:
        curr = pq.get()
        display(curr)
        if curr.cost ==0:
            print("--"*10)
            print("final solution state :\n")
            display(curr)
            return
        x , y = getZero(curr.puzzle)
        
        if x > 0:
            temp = copy.deepcopy(curr)
            temp.puzzle[x][y] , temp.puzzle[x-1][y] = temp.puzzle[x-1][y] , temp.puzzle[x][y]
            temp = calScore(temp , gl)
            if temp.puzzle not in vis:
                vis.append(temp.puzzle)
                pq.put(temp)
                
        if x < 2 :
            temp = copy.deepcopy(curr)
            temp.puzzle[x][y] , temp.puzzle[x+1][y] = temp.puzzle[x+1][y] , temp.puzzle[x][y]
            temp = calScore(temp , gl)
            if temp.puzzle not in vis:
                vis.append(temp.puzzle)
                pq.put(temp)
                
        if y > 0:
            temp = copy.deepcopy(curr)
            temp.puzzle[x][y] , temp.puzzle[x][y-1] = temp.puzzle[x][y-1] , temp.puzzle[x][y]
            temp = calScore(temp , gl)
            if temp.puzzle not in vis:
                vis.append(temp.puzzle)
                pq.put(temp)
                
        if y < 2:
            temp = copy.deepcopy(curr)
            temp.puzzle[x][y] , temp.puzzle[x][y+1] = temp.puzzle[x][y+1] , temp.puzzle[x][y]
            temp = calScore(temp , gl)
            if temp.puzzle not in vis:
                vis.append(temp.puzzle)
                pq.put(temp)
                
    print("success")
    
initial_puzzle = [[1,2, 3], [8, 6, 4], [7, 0, 5]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

solve(ini , gl)
