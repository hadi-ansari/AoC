from reader import read_problem
import itertools

def get_shortest_path(pair):
  path_lenght = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
#   print("Path length between: {} and {}\n{}".format(pair[0], pair[1],path_lenght))
  return path_lenght

def find_galaxies(graph):
   galaxies = []
   for y in range(len(graph)):
      for x in range(len(graph[0])) :
         if graph[y][x] == "#":
            galaxies.append((x, y))
    
   return galaxies

def print_graph(graph):
    print("width: ", len(graph[0]), "height: ", len(graph))
    for row in graph:
      formated_row = ""
      for pos in row:
         formated_row += pos
      print(formated_row)

def load_graph(content):
    temp_content = []
    for line in content:
       temp_content.append(line.strip())

    graph = []
    for i in range(len(temp_content)):
        row = []
        for j in range(len(temp_content[i])):
           row.append(temp_content[i][j])
        graph.append(row)
    return graph

def expand_universe(graph):
   temp_graph = []
   for row in graph:
      temp_graph.append(row)
      is_empty_row = True
      for pos in row:
        if pos != ".":
            is_empty_row = False
            break
      if is_empty_row:
        empty_row = []
        for x in range(len(row)):
           empty_row.append(".")
        temp_graph.append(empty_row)

   expanded_universe = list(temp_graph)
   offset = 0
   for x in range(len(temp_graph[0])):
      is_empty_col = True
      for y in range(len(temp_graph)):
         if(temp_graph[y][x] != "."):
            is_empty_col = False
            break
      temp_rows = []
      if is_empty_col:
         for row in expanded_universe:
            temp_row = list(row)
            temp_row.insert(x + offset , ".")
            temp_rows.append(temp_row)
         offset += 1
         expanded_universe = list(temp_rows)



   return expanded_universe


def main():
    content = read_problem("input-example.txt")
    graph = load_graph(content)
    graph = expand_universe(graph)
    galaxies = find_galaxies(graph)
    galaxy_pairs = list(itertools.combinations(galaxies, 2))
    sum = 0
    for pair in galaxy_pairs:
       sum += get_shortest_path(pair)


    print(sum)



main()