graph = {1: [[2, 1], [4, 3], [3, 4]],
         2: [[1, 1], [4, 2]],
         3: [[1, 4], [4, 5]],
         4: [[1, 3], [2, 2], [3, 5]]}

remaining_vertices = [x + 1 for x in range(len(graph))]
