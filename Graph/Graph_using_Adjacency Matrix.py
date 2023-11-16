def add_Node(v):
  global node_count
  if v in nodes:
    print('Node already present')
  else:
    node_count += 1
    nodes.append(v)
    for i in graph:
      i.append(0)
    temp = []
    for j in range(node_count):
      temp.append(0)
    graph.append(temp)

# For undirected and unweighted
def add_edge(v1, v2):
  if v1 not in nodes:
    print(v1, 'is not present in the graph')
  elif v2 not in nodes:
    print(v1, 'is not present in the graph')
  else:
    index1 = nodes.index(v1)    
    index2 = nodes.index(v2)
    graph[index1][index2] = 1    
    graph[index2][index1] = 1    

# For undirected and weighted
def add_edge(v1, v2, cost):
  if v1 not in nodes:
    print(v1, 'is not present in the graph')
  elif v2 not in nodes:
    print(v1, 'is not present in the graph')
  else:
    index1 = nodes.index(v1)    
    index2 = nodes.index(v2)
    graph[index1][index2] = cost    
    graph[index2][index1] = cost    

# For directed and unweighted
def add_edge(v1, v2):
  if v1 not in nodes:
    print(v1, 'is not present in the graph')
  elif v2 not in nodes:
    print(v1, 'is not present in the graph')
  else:
    index1 = nodes.index(v1)    
    index2 = nodes.index(v2)
    graph[index1][index2] = 1  

# For directed and weighted
def add_edge(v1, v2, cost):
  if v1 not in nodes:
    print(v1, 'is not present in the graph')
  elif v2 not in nodes:
    print(v1, 'is not present in the graph')
  else:
    index1 = nodes.index(v1)    
    index2 = nodes.index(v2)
    graph[index1][index2] = cost   


def delete_node(v):
  if v not in nodes:
    print(v,'is not present in the graph')
  else:
    index1 = nodes.index(v)
    node_count -= 1
    nodes.remove(v)
    graph.pop(index1)
    for i in graph:
      i.pop(index1)

def print_graph():
  for i in range(node_count):
    for j in range(node_count):
      print(format(graph[i][j],'<3'),end=' ')
    print()


nodes = []
graph = []
node_count = 0

add_Node('A')
add_Node('B')
add_Node('C')

add_edge('A','B')
add_edge('A','C')
add_edge('B','C')

add_Node('D')

delete_node('A')

print(graph)
print_graph()
