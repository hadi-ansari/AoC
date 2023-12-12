from reader import read_problem
import itertools


def bfs(graph, node):
  visited = []
  queue = [] 
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

def find_galaxies(graph):
   galaxies = []
   for row in graph:
      for col in row:
         if col[2] == "#":
            galaxies.append((col[0], col[1]))
    
   return galaxies

def print_graph(graph):
    for row in graph:
      formated_row = ""
      for pos in row:
         formated_row += pos[2]
      print(formated_row)

def load_graph(content):
    temp_content = []
    for line in content:
       temp_content.append(line.strip())

    graph = []
    for i in range(len(temp_content)):
        row = []
        for j in range(len(temp_content[i])):
           row.append((i, j, temp_content[i][j]))
        graph.append(row)
    return graph

def expand_universe(graph):
   temp_graph = []
   for row in graph:
      temp_graph.append(row)
      is_empty_row = True
      for pos in row:
        if pos[2] != ".":
            is_empty_row = False
      if is_empty_row:
        empty_row = []
        for i in range(len(row)):
           empty_row.append((row[i][0] + 1, row[i][1], "."))
        temp_graph.append(empty_row)


   temp_graph2 = temp_graph
   for i in range(len(temp_graph[0])):
      is_empty_col = True
      for line in temp_graph:
         if(line[i][2] != "."):
            is_empty_col = False
      if is_empty_col:
         for row in temp_graph2:
            row.insert(i + 1, (row[i][0] + 1, row[i][1], "."))



   return temp_graph2


def main():
    content = read_problem("input-example.txt")
    graph = load_graph(content)
    print("orginal universe: ")
    print_graph(graph)
    graph = expand_universe(graph)
    print("expanded universe: ")
    print_graph(graph)
    galaxies = find_galaxies(graph)
    print(galaxies)
    test = list(itertools.combinations(galaxies, 2))
    print(len(test))




main()