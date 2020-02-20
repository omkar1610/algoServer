#include <iostream>
#include <list>
#include <string>

using namespace std;

class Graph 
{ 
private:
    int V;    // No. of vertices 
  
    // Pointer to an array containing adjacency lists 
    list<int> *adj;    
public: 
    Graph(int V)  // Constructor 
    { 
	    this->V = V; 
	    adj = new list<int>[V]; 
	} 
  
    // function to add an edge to graph 
    void addEdge(int v, int w)
    { 
	    adj[v].push_back(w); // Add w to v’s list. 
	}
  
    // prints BFS traversal from a given source s 
    void BFS(int s)
    { 
	    // Mark all the vertices as not visited 
	    bool *visited = new bool[V]; 
	    for(int i = 0; i < V; i++) 
	        visited[i] = false; 
	  
	    // Create a queue for BFS 
	    list<int> queue; 
	  
	    // Mark the current node as visited and enqueue it 
	    visited[s] = true; 
	    queue.push_back(s); 
	  
	    // 'i' will be used to get all adjacent 
	    // vertices of a vertex 
	    list<int>::iterator i; 
	  
	    while(!queue.empty()) 
	    { 
	        // Dequeue a vertex from queue and print it 
	        s = queue.front(); 
	        cout << s << " "; 
	        queue.pop_front(); 
	  
	        // Get all adjacent vertices of the dequeued 
	        // vertex s. If a adjacent has not been visited,  
	        // then mark it visited and enqueue it 
	        for (i = adj[s].begin(); i != adj[s].end(); ++i) 
	        { 
	            if (!visited[*i]) 
	            { 
	                visited[*i] = true; 
	                queue.push_back(*i); 
	            } 
	        } 
	    } 
	} 
}; 
  

int main() 
{ 
    // Create a graph given in the above diagram 
 
    // Graph g(4); 
    // g.addEdge(0, 1); 
    // g.addEdge(1, 0); 
    // g.addEdge(1, 2); 
    // g.addEdge(2, 1); 
    // g.addEdge(2, 3); 
    // g.addEdge(3, 2); 
  
    // cout << "Following is Breadth First Traversal "<< "(starting from vertex 2) \n"; 
    // g.BFS(1); 
    // printf("\n");

 
    int n, tmp, start;
    // fscanf(fp, "%d", &n);fscanf(fp, "%d", &start);

    FILE *stream = fopen("input.txt","r");
	// string line = NULL;
	char *line = NULL;
	size_t len = 0;
	ssize_t nread;

	if((nread = getline(&line, &len, stream)) != -1)
	{
		sscanf (line,"%d %d",&n,&start);
		cout<<n<<" "<<start<<endl;
		free(line);
	}

	for (int i = 0; i < n; ++i)
	{
		getline(&line, &len, stream);
		// printf("Retrieved line of length %zu:\n", nread);
		cout<<line<<endl;
		free(line);
		// istringstream is(line);
		// int n;
		// while( is >> n ) 
		// {
		// 	cout<<n<<endl;
		// }
	}

	
	fclose(stream);



  
    return 0; 
}