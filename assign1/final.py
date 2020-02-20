from collections import defaultdict
import sys
class Graph:
    def __init__(self, input_file):
        
        self.graph = defaultdict(set)
        self.cycle = False
        self.bipartite = True
        self.pair_bipartite = [-1,-1]
        self.pair_cycle = [-1,-1]
        self.populate_graph(input_file)
    
    def populate_graph(self, input_file):
        
        file = open(input_file, "r");
        first = file.readline()[:-1].split()
        self.vertices = int(first[0])

        u = 1
        for line in file:
            for num in line.split():
                self.graph[u].add(int(num))
                self.graph[int(num)].add(u)
            u += 1
        file.close()
        
        self.visited = [False] * (1 + len(self.graph)) 
        self.parent = [-1] * (1 + len(self.graph)) 
        self.level = [-1] * (1 + len(self.graph))
        
    def bfs(self, start):
        queue = [] 
        queue.append(start) 

        self.visited[start] = True
        self.level[start] = 1
        
        while queue: 
            s = queue.pop(0) 
            print (s, end = " ") 


            for neighbour in self.graph[s]: 
#                 print("\nhere s neigh", s, neighbour, self.cycle)
                if self.visited[neighbour] == False:
                    if self.parent[neighbour] == -1:
                        self.parent[neighbour] = s
                    if self.level[neighbour] == -1:
                        self.level[neighbour] = self.level[s] + 1

                    queue.append(neighbour) 
                    self.visited[neighbour] = True
                else:
                    if self.level[s] == self.level[neighbour]:
#                             print("\n",s, "==level==", neighbour)
                        self.pair_bipartite = [s, neighbour]
                        self.bipartite = False

                    if self.parent[neighbour] != -1 and self.parent[s] != neighbour:
#                         print("\n",s, "is not par of", neighbour)
                        self.cycle = True
                        self.pair_cycle = [s, neighbour]

        
        
    def BFS(self):
        print("BFS :", end = " ")
        for i in range(1, 1 + len(self.graph)):
            if self.visited[i] == False:
                self.bfs(i)

                
    def prob_3(self): # show_bipartite
        if self.bipartite:
            print("Yes !! Bipartite Levels : ", end = "")
            level = [i%2 for i in self.level[1:]]
        #     print(level)
            print("( ", end="")
            for i, num in enumerate(level):
                if num == 1:
                    print(i+1, end=" ")
            print(") ( ", end="")

            for i, num in enumerate(level):
                if num == 0:
                    print(i+1, end=" ")
            print(")")
        else:
            print("No !!\nNot Bipartite")
        
    def show_path_root(self, v):
        path = []
        while(v != -1):
            path.append(v)
            v = self.parent[v]
        return path[::-1]

    def prob_2(self): # Print Cycle
        if self.cycle:
            print("Yes !!\nCycle Exists : ", end = "")
            l1, l2 = self.show_path_root(self.pair_cycle[0]), self.show_path_root(self.pair_cycle[1])
            # print("Showing Cycles :\n", l1,l2)
            for i in range(1,min(len(l1), len(l2))):
                if l1[i] != l2[i]:
                    break
            res = l1[i-1:] + l2[:i-1:-1] + l1[i-1:i]
            print(res)
        else:
            print("No Cycle !!")


def assign1(input):
    g = Graph(input)

    # print(g.graph)
    print("Problem 1 : BFS")
    g.BFS()
    # print("\nParent :", g.parent[1:], "\nLevel :", g.level[1:])
    # print("\nisBipartite :", g.bipartite, "\t\thasCycle : ", g.cycle, 
    #       "\nBipartite Pair : ", g.pair_bipartite, "\tCycle Pair : ", g.pair_cycle )
    print("\n\nProblem 2 : Cycle")
    g.prob_2()
    print("\n\nProblem 3 : Bipartite")
    g.prob_3()

if  __name__ == '__main__':
    if len(sys.argv) != 2 : # == argc
        # Note the printf-like syntax below
        sys.exit('Usage: %s <input file name>' % sys.argv[0])            
    
    assign1(sys.argv[1])
    
