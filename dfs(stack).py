from stack import Stack

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

def dfs(maze, start, goal):
    offsets = {"up":(-1, 0), "right":(0, 1), "down":(1, 0), "left":(-1, 0)}
    stack = Stack()
    stack.push(start)
    predecessors = {start: None}

    while not stack.is_empty():
        current_cell = stack.pop()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                stack.push(neighbour)
                predecessors[neighbour] = current_cell

if __name__ == "__main__":
    # Pruebas
    maze = [[0] * 3 for row in range(3)]
    maze[0][1] = '*'
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = dfs(maze, start_pos, goal_pos)
    print(result)