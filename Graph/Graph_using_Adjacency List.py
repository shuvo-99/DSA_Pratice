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
    print(v2, 'is not present in the graph')
  else:
    graph[v1].append(v2)
    graph[v2].append(v1)

# For undirected and weighted
def add_edge(v1, v2, cost):
  if v1 not in graph:
    print(v1, 'is not present in the graph')
  elif v2 not in graph:
    print(v2, 'is not present in the graph')
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
    print(v2, 'is not present in the graph')
  else:
    graph[v1].append(v2)

# For directed and weighted
def add_edge(v1, v2, cost):
  if v1 not in graph:
    print(v1, 'is not present in the graph')
  elif v2 not in graph:
    print(v2, 'is not present in the graph')
  else:
    lst1 = [v2, cost]
    graph[v1].append(lst1)

# For unweighted
def delete_node(v):
  if v not in graph:
    print(v, 'is not present in the graph')
  else:
    graph.pop(v)
    for i in graph:
      list1 = graph[i]
      if v in list1:
        list1.remove(v)

# For weighted
def delete_node(v):
  if v not in graph:
    print(v, 'is not present in the graph')
  else:
    graph.pop(v)
    for i in graph:
      list1 = graph[i]
      for j in list1:
        if v == j[0]:
          list1.remove(j)
          break

# For undirected and unweighted
def delete_edge(v1,v2):
  if v1 not in graph:
    print(v1, 'is not present in the graph')
  elif v2 not in graph:
    print(v2, 'is not present in the graph')
  else:
    if v2 in graph[v1]:
      graph[v1].remove(v2)
      graph[v2].remove(v1)

# For undirected and weighted
def delete_edge(v1,v2,cost):
  if v1 not in graph:
    print(v1, 'is not present in the graph')
  elif v2 not in graph:
    print(v2, 'is not present in the graph')
  else:
    temp1 = [v1, cost]
    temp2 = [v2, cost]
    if temp2 in graph[v1]:
      graph[v1].remove(temp2)
      graph[v2].remove(temp1)

# For directed and unweighted
def delete_edge(v1,v2):
  if v1 not in graph:
    print(v1, 'is not present in the graph')
  elif v2 not in graph:
    print(v2, 'is not present in the graph')
  else:
    if v2 in graph[v1]:
      graph[v1].remove(v2)

# For directed and weighted
def delete_edge(v1,v2,cost):
  if v1 not in graph:
    print(v1, 'is not present in the graph')
  elif v2 not in graph:
    print(v2, 'is not present in the graph')
  else:
    temp = [v2, cost]
    if temp in graph[v1]:
      graph[v1].remove(temp)

  


graph = {}

add_Node('A')
add_Node('B')
add_Node('C')

# add_edge('A','B')
add_edge('A','B',5)

delete_node('B')
# delete_edge('A','B')

print(graph)
