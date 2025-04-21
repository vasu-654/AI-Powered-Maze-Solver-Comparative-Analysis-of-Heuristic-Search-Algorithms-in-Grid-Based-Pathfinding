import math
import heapq
import random
import time
import matplotlib.pyplot as plt

# Maze dimensions
ROWS = 20
COLS = 20

# Constants for cell types
EMPTY = 0
WALL = 1
START = 2
DESTINATION = 3

# Global variable to count comparisons
comparisons_count = 0

# Heuristic functions
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def diagonal_distance(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return max(dx, dy)

def chebyshev_distance(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return max(dx, dy)

# Helper function to create a randomized maze
def create_maze():
    maze = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    # Generate random walls
    for i in range(1, ROWS-1):
        for j in range(1, COLS-1):
            if random.random() < 0.3:
                maze[i][j] = WALL
    # Set start and destination
    start = (1, 1)
    destination = (ROWS-2, COLS-2)
    maze[start[0]][start[1]] = START
    maze[destination[0]][destination[1]] = DESTINATION
    return maze, start, destination

# Flood fill algorithm
def flood_fill(maze, start, destination):
    visited = set()
    stack = [start]
    came_from = {}

    while stack:
        current = stack.pop()
        visited.add(current)
        if current == destination:
            return reconstruct_path(came_from, start, destination), len(visited)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                came_from[neighbor] = current
                stack.append(neighbor)

    return [], len(visited)

# A* algorithm
def a_star(maze, start, destination, heuristic):
    global comparisons_count
    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, destination)}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == destination:
            return reconstruct_path(came_from, start, destination), comparisons_count
        for neighbor in get_neighbors(current, maze):
            comparisons_count += 1
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, destination)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return [], comparisons_count

# Helper function to get valid neighbors of a cell
def get_neighbors(cell, maze):
    neighbors = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        x, y = cell[0] + dx, cell[1] + dy
        if 0 <= x < ROWS and 0 <= y < COLS and maze[x][y] != WALL:
            neighbors.append((x, y))
    return neighbors

# Helper function to reconstruct the path
def reconstruct_path(came_from, start, destination):
    current = destination
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

# Display the maze with movements using Matplotlib
def display_maze_with_movements(maze, movements):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')

    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) in movements:
                ax.add_patch(plt.Rectangle((j, ROWS - 1 - i), 1, 1, color='green'))
            elif maze[i][j] == EMPTY:
                ax.add_patch(plt.Rectangle((j, ROWS - 1 - i), 1, 1, color='white'))
            elif maze[i][j] == WALL:
                ax.add_patch(plt.Rectangle((j, ROWS - 1 - i), 1, 1, color='black'))
            elif maze[i][j] == START:
                ax.add_patch(plt.Rectangle((j, ROWS - 1 - i), 1, 1, color='blue'))
            elif maze[i][j] == DESTINATION:
                ax.add_patch(plt.Rectangle((j, ROWS - 1 - i), 1, 1, color='red'))

    ax.set_xlim(0, COLS)
    ax.set_ylim(0, ROWS)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()

# Function to run A* algorithm with Manhattan distance heuristic
def run_a_star_manhattan(maze, start, destination):
    # maze, start, destination = create_maze()
    # print("Initial Maze:")
    # display_maze_with_movements(maze, [])

    comparisons = {}

    print("\nA* with Manhattan Distance Heuristic:")
    global comparisons_count
    comparisons_count = 0
    start_time = time.time()
    movements_manhattan, comparisons["Manhattan"] = a_star(maze, start, destination, manhattan_distance)
    end_time = time.time()
    display_maze_with_movements(maze, movements_manhattan)
    print("Total movements:", len(movements_manhattan))
    print("Time taken:", end_time - start_time, "seconds")
    print("Comparisons:", comparisons["Manhattan"])

# Function to run A* algorithm with Euclidean distance heuristic
def run_a_star_euclidean(maze, start, destination):
    # maze, start, destination = create_maze()
    # print("Initial Maze:")
    # display_maze_with_movements(maze, [])

    comparisons = {}

    print("\nA* with Euclidean Distance Heuristic:")
    global comparisons_count
    comparisons_count = 0
    start_time = time.time()
    movements_euclidean, comparisons["Euclidean"] = a_star(maze, start, destination, euclidean_distance)
    end_time = time.time()
    display_maze_with_movements(maze, movements_euclidean)
    print("Total movements:", len(movements_euclidean))
    print("Time taken:", end_time - start_time, "seconds")
    print("Comparisons:", comparisons["Euclidean"])

# Function to run A* algorithm with Diagonal distance heuristic
def run_a_star_diagonal(maze, start, destination):
    # maze, start, destination = create_maze()
    # print("Initial Maze:")
    # display_maze_with_movements(maze, [])

    comparisons = {}

    print("\nA* with Diagonal Distance Heuristic:")
    global comparisons_count
    comparisons_count = 0
    start_time = time.time()
    movements_diagonal, comparisons["Diagonal"] = a_star(maze, start, destination, diagonal_distance)
    end_time = time.time()
    display_maze_with_movements(maze, movements_diagonal)
    print("Total movements:", len(movements_diagonal))
    print("Time taken:", end_time - start_time, "seconds")
    print("Comparisons:", comparisons["Diagonal"])

# Function to run A* algorithm with Chebyshev distance heuristic
def run_a_star_chebyshev(maze, start, destination):
    # maze, start, destination = create_maze()
    # print("Initial Maze:")
    # display_maze_with_movements(maze, [])

    comparisons = {}

    print("\nA* with Chebyshev Distance Heuristic:")
    global comparisons_count
    comparisons_count = 0
    start_time = time.time()
    movements_chebyshev, comparisons["Chebyshev"] = a_star(maze, start, destination, chebyshev_distance)
    end_time = time.time()
    display_maze_with_movements(maze, movements_chebyshev)
    print("Total movements:", len(movements_chebyshev))
    print("Time taken:", end_time - start_time, "seconds")
    print("Comparisons:", comparisons["Chebyshev"])

# Function to run Flood Fill algorithm
def run_flood_fill(maze, start, destination):
    # maze, start, destination = create_maze()
    # print("Initial Maze:")
    # display_maze_with_movements(maze, [])

    print("\nFlood Fill Algorithm:")
    start_time = time.time()
    movements_flood_fill, visited_cells = flood_fill(maze, start, destination)
    end_time = time.time()
    display_maze_with_movements(maze, movements_flood_fill)
    print("Total movements:", len(movements_flood_fill))
    print("Visited cells:", visited_cells)
    print("Time taken:", end_time - start_time, "seconds")

if __name__ == "__main__":
    maze, start, destination = create_maze()
    print("Initial Maze:")
    display_maze_with_movements(maze, [])
    run_a_star_manhattan(maze, start, destination)
    run_a_star_euclidean(maze, start, destination)
    run_a_star_diagonal(maze, start, destination)
    run_a_star_chebyshev(maze, start, destination)
    run_flood_fill(maze, start, destination)
