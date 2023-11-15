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


def print_graph():
  for i in range(node_count):
    for j in range(node_count):
      print(graph[i][j],end=' ')
    print()


nodes = []
graph = []
node_count = 0
add_Node('A')
add_Node('B')
add_Node('C')
add_Node('D')
add_Node('E')
add_Node('F')

print(graph)
print_graph()
