def add_Node(v):
  
  if v in graph:
    print('Node already present')
  else:
    graph[v] = []


graph = {}

add_Node('A')
add_Node('B')
add_Node('C')

print(graph)
