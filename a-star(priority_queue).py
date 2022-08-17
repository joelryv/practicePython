from priority_queue import PriorityQueue

def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def is_legal_pos(maze, neighbour):
    return not(neighbour[0] < 0 or neighbour[1] < 0 
            or neighbour[0] >= len(maze) or neighbour[1] >= len(maze[0])
            or maze[neighbour[0]][neighbour[1]] == '*')

def get_path(predecessors, start, goal):
    current = goal
    path = [current]
    while current != start:
        path.append(predecessors[current])
        current = predecessors[current]
    return path[::-1]

def a_star(maze, start, goal):
    offsets = {"up":(-1, 0), "right":(0, 1), "down":(1, 0), "left":(-1, 0)}
    pq = PriorityQueue()
    pq.put(start, 0)
    predecessors = {start: None}
    g_values = {start: 0}

    while not pq.is_empty():
        current_cell = pq.get()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in g_values:
                new_cost = g_values[current_cell] + 1
                g_values[neighbour] = new_cost
                f_value = new_cost + heuristic(goal, neighbour)
                pq.put(neighbour, f_value)
                predecessors[neighbour] = current_cell

if __name__ == "__main__":
    # Pruebas
    maze = [[0] * 3 for row in range(3)]
    maze[0][1] = '*'
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    print(result)