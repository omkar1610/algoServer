#include <iostream>
#include <sstream>
#include <fstream>
#include <list>

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

	bool isCyclicConntected(vector<int> adj[], int s, 
                        int V, vector<bool>& visited) 
	{ 
	    // Set parent vertex for every vertex as -1. 
	    vector<int> parent(V, -1); 
	  
	    // Create a queue for BFS 
	    queue<int> q; 
	  
	    // Mark the current node as visited and enqueue it 
	    visited[s] = true; 
	    q.push(s); 
	  
	    while (!q.empty()) { 
	  
	        // Dequeue a vertex from queue and print it 
	        int u = q.front(); 
	        q.pop(); 
	  
	        // Get all adjacent vertices of the dequeued 
	        // vertex u. If a adjacent has not been visited, 
	        // then mark it visited and enqueue it. We also 
	        // mark parent so that parent is not considered 
	        // for cycle. 
	        for (auto v : adj[u]) { 
	            if (!visited[v]) { 
	                visited[v] = true; 
	                q.push(v); 
	                parent[v] = u; 
	            } 
	            else if (parent[u] != v) 
	                return true; 
	        } 
	    } 
	    return false; 
	} 
}; 
  
int main(int argc, char const *argv[])
{
	int tmp, n, start;
	string line;

	ifstream file("input.txt");
	getline(file, line);
	
	istringstream is(line);
	is >> n;
	is >> start;
	start--;

	cout<<n<<start<<endl;

	Graph g(n); 
    
  
    cout << "Following is Breadth First Traversal "<< "(starting from vertex "<<start+1<<") \n"; 
    g.BFS(1); 
    printf("\n");



	for (int i = 0; i < n; ++i)
	{
		getline(file, line);
		// cout<<line<<": ";
		istringstream is(line);
		
		while( is >> tmp ) {
		  cout<<tmp<<", ";
		  g.addEdge(i, tmp-1); 
		}
		cout<<endl;
	}
	file.close();
	g.BFS(start); 
    printf("\n");
	return 0;
}