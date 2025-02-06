# Ford-Fulkerson Algorithm for Maximum Flow

## Overview
This project implements the **Ford-Fulkerson algorithm** to find the maximum possible flow in a directed graph with **7 nodes** and **12 edges**. The graph is built using user-defined capacities for each edge. The program also provides a **visualization** of the graph using **Matplotlib** and **NetworkX**.

## Features
- **Input custom capacities** for 12 edges in the graph.
- **Graph representation** using adjacency list.
- **Breadth-First Search (BFS)** for augmenting paths.
- **Ford-Fulkerson method** to compute the maximum flow.
- **Graph visualization** with edge capacities displayed.

## Prerequisites
Ensure you have the following Python libraries installed:
```sh
pip install matplotlib networkx
```

## How It Works
1. **User Input:** The program prompts the user to enter capacities for **12 edges** in the graph.
2. **Graph Construction:** The graph is created using an adjacency list where each edge has a **forward capacity** and a **reverse edge with zero initial capacity**.
3. **Algorithm Execution:** The **Ford-Fulkerson algorithm** iteratively finds augmenting paths using **BFS**, updates the residual capacities, and accumulates the maximum flow.
4. **Visualization:** The graph is displayed with **nodes, edges, and capacities**.
5. **Result Display:** The maximum possible flow from **source (node 1)** to **sink (node 7)** is computed and printed.

## Graph Structure
The graph consists of:
- **7 nodes** labeled **1 to 7**
- **12 directed edges**

### **Edges and User-Defined Capacities**
| Edge         | Input Variable |
|-------------|---------------|
| 1 → 2      | x1            |
| 1 → 3      | x2            |
| 2 → 4      | x3            |
| 2 → 5      | x4            |
| 3 → 4      | x5            |
| 3 → 6      | x6            |
| 4 → 5      | x7            |
| 4 → 6      | x8            |
| 5 → 7      | x9            |
| 6 → 7      | x10           |
| 2 → 3      | x11           |
| 5 → 6      | x12           |

## Usage
Run the script and enter the capacities for each edge when prompted:
```sh
python ford_fulkerson.py
```
After entering the values, the script will:
- Display the graph.
- Compute and print the maximum flow.

## Example Output
```sh
Enter the capacity for edge (1 -> 2): 10
Enter the capacity for edge (1 -> 3): 5
...
The maximum possible flow is: 15
```

## Visualization
The program generates a directed graph where:
- **Nodes** are represented in blue.
- **Edges** are drawn with **capacities labeled in red**.

## Ford-Fulkerson Algorithm Steps
1. **Initialize** flow as 0.
2. **Find an augmenting path** using BFS.
3. **Find the minimum residual capacity** along the path.
4. **Update the residual capacities** in the network.
5. **Repeat until no augmenting path exists**.


