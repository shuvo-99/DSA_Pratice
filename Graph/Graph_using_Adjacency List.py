def add_Node(v):
  
  if v in graph:
    print('Node already present')
  else:
    graph[v] = []

# For undirected and unweighted
def add_edge(v1, v2):
  if v1 not in graph:
    print(v1, 'is not present in the graph')
  elif v2 not in graph:
    print(v1, 'is not present in the graph')
  else:
    graph[v1].append(v2)
    graph[v2].append(v1)

# For undirected and weighted
def add_edge(v1, v2, cost):
  if v1 not in graph:
    print(v1, 'is not present in the graph')
  elif v2 not in graph:
    print(v1, 'is not present in the graph')
  else:
    lst1 = [v2, cost]
    lst2 = [v1, cost]
    graph[v1].append(lst1)
    graph[v2].append(lst2)

# For directed and unweighted
def add_edge(v1, v2):
  if v1 not in graph:
    print(v1, 'is not present in the graph')
  elif v2 not in graph:
    print(v1, 'is not present in the graph')
  else:
    graph[v1].append(v2)

# For directed and weighted
def add_edge(v1, v2, cost):
  if v1 not in graph:
    print(v1, 'is not present in the graph')
  elif v2 not in graph:
    print(v1, 'is not present in the graph')
  else:
    lst1 = [v2, cost]
    graph[v1].append(lst1)

graph = {}

add_Node('A')
add_Node('B')
add_Node('C')

add_edge('A','B')
add_edge('A','B',5)

print(graph)
