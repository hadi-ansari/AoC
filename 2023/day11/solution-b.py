from reader import read_problem
import copy
import itertools

# 1000000
EXPANSION_RATE = 1000000

def get_shortest_path(pair):
  path_lenght = abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
#   print("Path length between: {} and {}\n{}".format(pair[0], pair[1], path_lenght))
  return path_lenght

def find_galaxies(graph, empty_rows_idx, empty_cols_idx):
   galaxies = []
   for y in range(len(graph)):
      for x in range(len(graph[0])) :
         if graph[y][x] == "#":
            galaxies.append([x, y])

   updated_rows = copy.deepcopy(galaxies)
   for r in empty_rows_idx:
       for i in range(len(galaxies)):
          if r <= galaxies[i][1]:
             updated_rows[i][1] += EXPANSION_RATE - 1

   updated_galaxies = copy.deepcopy(updated_rows)
   for c in empty_cols_idx:
      for i in range(len(galaxies)):
          if c < galaxies[i][0]:
             updated_galaxies[i][0] += EXPANSION_RATE - 1
             
   return updated_galaxies

def draw_universe(galaxies):
   universe_height = max(list(map(lambda v: v[1], galaxies))) + 1
   universe_width = max(list(map(lambda v: v[0], galaxies))) + 1
   print(universe_width, " X ", universe_height)
   for y in range(universe_height):
      row = ""
      for x in range(universe_width):
         if [x, y] not in galaxies:
            row+="."
         else:
            row += "#"
      print(row)

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

def find_expand_indexes(graph):
   row_len = len(graph[0])
   col_len = len(graph)
   empty_rows_idx = []
   empty_cols_idx = []
   for y in range(col_len):
      empty_row_index = y
      for x in range(row_len):
        if graph[y][x] != ".":
            empty_row_index = -1
            break
      if empty_row_index != -1:
         empty_rows_idx.append(empty_row_index)

   for x in range(row_len):
      empty_col_index = x
      for y in range(col_len):
        if graph[y][x] != ".":
            empty_col_index = -1
            break
      if empty_col_index != -1:
         empty_cols_idx.append(empty_col_index)

    
   return empty_rows_idx, empty_cols_idx

def main():
    content = read_problem("input.txt")
    graph = load_graph(content)
    empty_rows_idx, empty_cols_idx = find_expand_indexes(graph)
  
    galaxies = find_galaxies(graph, empty_rows_idx, empty_cols_idx)
  
    galaxy_pairs = list(itertools.combinations(galaxies, 2))

    sum = 0
    for pair in galaxy_pairs:
       sum += get_shortest_path(pair)
    print(sum)



main()
