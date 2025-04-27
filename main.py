from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    vertices = set(graph.keys())
    for neighbors in graph.values():
        for v, _ in neighbors:
            vertices.add(v)
    
    # Priority queue: (total_weight, num_edges, vertex)
    heap = []
    heappush(heap, (0, 0, source))
    
    # Initialize distances for all vertices
    distances = {v: (float('inf'), float('inf')) for v in vertices}
    distances[source] = (0, 0)
    
    while heap:
        total_weight, num_edges, u = heappop(heap)
        
        if u not in graph:
            continue  # If no outgoing edges from u
        
        for v, weight in graph[u]:
            new_weight = total_weight + weight
            new_edges = num_edges + 1
            
            # Relaxation step: prefer smaller weight, or same weight with fewer edges
            if (new_weight < distances[v][0]) or (new_weight == distances[v][0] and new_edges < distances[v][1]):
                distances[v] = (new_weight, new_edges)
                heappush(heap, (new_weight, new_edges, v))
    
    return distances

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    parent = {}
    visited = set()
    queue = deque()

    visited.add(source)
    queue.append(source)

    while queue:
        u = queue.popleft()
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                queue.append(v)
    return parent
    pass

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = []
    current = destination

    while current in parents:
        current =  parents[current]
        path.append(current)

    path.reverse()
    return ''.join(path)
    pass
