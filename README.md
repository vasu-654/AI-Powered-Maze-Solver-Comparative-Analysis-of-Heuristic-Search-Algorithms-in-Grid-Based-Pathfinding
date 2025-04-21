# AI-Powered Maze Solver: Heuristic Search & Visualization

This project is a comprehensive simulation of AI-based pathfinding algorithms on a dynamically generated 2D maze environment. It leverages various heuristic functions to evaluate and compare the performance of the A* algorithm alongside a classical uninformed search strategy (Flood Fill). Visualization is integrated using Matplotlib for intuitive understanding of search behaviors.

---

## 🚀 Key Features

- **Dynamic Maze Generation**: Procedurally generates randomized mazes with configurable dimensions.
- **A* Search Algorithm**: Implements A* with multiple heuristic functions:
  - Manhattan Distance
  - Euclidean Distance
  - Diagonal Distance
  - Chebyshev Distance
- **Flood Fill Algorithm**: Included as a baseline uninformed search method.
- **Heuristic Evaluation Metrics**:
  - Number of node comparisons
  - Total path length
  - Execution time
- **Visual Representation**: Real-time visualization of search paths, obstacles, and search areas using `matplotlib`.

---

## 🧠 Technical Concepts & AI Alignment

- **Artificial Intelligence**: Demonstrates core AI search strategies including informed (A*) and uninformed (Flood Fill) search.
- **Heuristics**: Utilizes admissible and consistent heuristic functions for A* to guide search more efficiently.
- **Pathfinding**: A foundational problem in robotics, game AI, and autonomous agents.
- **Algorithmic Analysis**: Tracks and compares computational cost and effectiveness of each approach.

---

## 🧰 Requirements

- Python 3.x
- matplotlib

Install dependencies:

pip install matplotlib
**🧪 How It Works**

◉ Generate a random maze (create_maze()).
◉ Run each search algorithm:
◉ a_star(heuristic=manhattan_distance)
◉ a_star(heuristic=euclidean_distance)
◉ a_star(heuristic=diagonal_distance)
◉ a_star(heuristic=chebyshev_distance)
◉ flood_fill()
◉ Visualize and benchmark:
◉ Display search path
◉ Print number of movements, comparisons, and runtime

**▶️ Example Execution**

Run the main script:
python maze_solver.py

**Output includes:**

◉ Maze grid visualization
◉ Search path in green
◉ Start and destination highlighted
◉ Performance metrics printed in console

**📊 Performance Metrics**

◉ Each algorithm run provides:
◉ Total path length (movement steps)
◉ Search comparisons (visited nodes)
◉ Execution time (in seconds)

**📌 Future Enhancements**

◉ Support for diagonal movement in flood fill
◉ Weighted grid support (Dijkstra variant)
◉ Interactive UI (Tkinter or Web-based)
◉ Real-time step-by-step animation
