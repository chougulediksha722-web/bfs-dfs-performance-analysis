# SLE-3: Full C4 Architecture Design

## System Title
BFS and DFS Graph Search System

## System Description
This system implements Breadth First Search (BFS) and Depth First Search (DFS)
for graph traversal and search. It compares the performance of both algorithms
using execution-time measurement and profiling. The system continues the work
from SLE-2.

## C4 Architecture

### Level 1 – Context
Shows the BFS and DFS Graph Search System and its interaction with the User
and Graph Data.

### Level 2 – Container
The main containers are:
- Graph Input Module
- BFS Search Module
- DFS Search Module
- Performance Measurement Module
- Profiling Module
- Output Module

### Level 3 – Component
The BFS Search Module is divided into:
- Queue / Frontier
- Visited Manager
- Neighbor Expansion
- Goal Test

### Level 4 – Code
The code level shows the main Python files used in the implementation:
- bfs.py
- dfs.py
- graph_data.py
- sle2_profiling.py
- pyspy_target.py

## Design Decisions
- BFS and DFS are kept as separate search modules.
- Performance measurement and profiling are separated from search logic.
- The architecture follows all four C4 levels.
- The design continues the implementation from SLE-2.

## AI Contribution
ChatGPT and GitHub Copilot were used for programming concepts,
code suggestions, troubleshooting, explanations and documentation support.
The student reviewed AI suggestions, implemented and tested the work,
and made the final design decisions.

## Conclusion
The C4 architecture provides a clear view of the BFS and DFS Graph Search
System from system context to code level and connects the SLE-2 implementation
with the SLE-3 architectural design.