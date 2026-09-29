SLE-2: BFS vs DFS Performance Analysis

Overview

This project is part of SLE-2 and focuses on the performance analysis of two fundamental graph traversal algorithms:

* Breadth-First Search (BFS)
* Depth-First Search (DFS)

The project implements both algorithms on the same graph and compares their execution time and the number of nodes expanded.

The project also uses Python profiling tools to analyze algorithm execution and generate visual profiling outputs.



Objectives

The main objectives of this project are:

1. Implement BFS and DFS.
2. Execute both algorithms on the same graph.
3. Measure execution time.
4. Count the number of nodes expanded.
5. Analyze the algorithms using cProfile.
6. Generate profiling visualizations.
7. Use py-spy for sampling-based profiling.
8. Store the profiling results as SVG flamegraphs.
9. Document the complete analysis in GitHub.



Algorithms

Breadth-First Search (BFS)

BFS explores a graph level by level. It uses a queue to keep track of nodes that need to be explored.

Depth-First Search (DFS)

DFS explores a path as deeply as possible before backtracking. It can be implemented using recursion or a stack.

Both algorithms are executed using the same graph and start/goal nodes for comparison.



Project Structure

sle 2/
│
├── profiling/
│   ├── bfs.prof
│   ├── bfs_profile.svg
│   ├── dfs.prof
│   ├── dfs_profile.svg
│   ├── bfs_clean.prof
│   ├── dfs_clean.prof
│   ├── bfs_clean.svg
│   ├── pyspy_bfs.svg
│   └── pyspy_dfs.svg
│
├── report 1/
│   └── sle2(AI)26UAM310.docx
│
├── results/
│   └── results.txt
│
├── .gitignore
├── CONTRIBUTION_LOG.md
├── README.md
├── graph_data.py
├── pyspy_target.py
├── pyspy_bfs_target.py
├── pyspy_dfs_target.py
├── profile_bfs.py
├── profile_dfs.py
└── sle2_profiling.py




Running the BFS and DFS Comparison

Run the main profiling/performance program with:

py -3.12 sle2_profiling.py

Example output:

BFS
Total time: 9.205100 ms
Nodes expanded: 7
DFS
Total time: 4.285200 ms
Nodes expanded: 3

The exact execution time may change between runs depending on the system and Python runtime.




cProfile Analysis

The project uses Python’s built-in cProfile module for detailed profiling.

BFS Profiling

Run:

py -3.12 profile_bfs.py

This generates:

profiling/bfs_clean.prof

The profiling data can then be converted into an SVG visualization.

DFS Profiling

Run:

py -3.12 profile_dfs.py

This generates:

profiling/dfs_clean.prof




py-spy Profiling

py-spy is also used to collect runtime sampling data and generate flamegraph SVG files.

The project uses Python 3.14 for the py-spy target processes.

Check py-spy

& "C:\Users\hp\AppData\Local\Programs\Python\Python314\Scripts\py-spy.exe" --version

BFS py-spy Profiling

Run:

& "C:\Users\hp\AppData\Local\Programs\Python\Python314\Scripts\py-spy.exe" record --format flamegraph --output profiling/pyspy_bfs.svg --duration 10 -- "C:\Users\hp\AppData\Local\Programs\Python\Python314\python.exe" pyspy_bfs_target.py

The output is:

profiling/pyspy_bfs.svg

DFS py-spy Profiling

Run:

& "C:\Users\hp\AppData\Local\Programs\Python\Python314\Scripts\py-spy.exe" record --format flamegraph --output profiling/pyspy_dfs.svg --duration 10 -- "C:\Users\hp\AppData\Local\Programs\Python\Python314\python.exe" pyspy_dfs_target.py

The output is:

profiling/pyspy_dfs.svg

These SVG files can be opened in a web browser to view the profiling flamegraphs.




Performance Results

The current recorded execution produced:

Algorithm	Total Time	Nodes Expanded
BFS	9.205100 ms	7
DFS	4.285200 ms	3

These values are recorded in:

results/results.txt

Performance measurements can vary slightly between executions.




Profiling Outputs

The repository contains profiling outputs generated using different tools.

cProfile

profiling/bfs_clean.prof
profiling/dfs_clean.prof
profiling/bfs_clean.svg

py-spy

profiling/pyspy_bfs.svg
profiling/pyspy_dfs.svg

The SVG files provide visual profiling representations of the algorithm execution.




Technologies Used

* Python
* BFS
* DFS
* Git
* GitHub
* GitHub Copilot
* cProfile
* flameprof
* py-spy
* SVG flamegraphs




AI Assistance

AI Coding Tool: GitHub Copilot

GitHub Copilot was used as an AI coding assistant during the development and documentation of the project.




Repository

GitHub Repository:

https://github.com/chougulediksha722-web/bfs-dfs-performance-analysis




Author

Diksha Chouguule

GitHub: chougulediksha722-web

⸻

Conclusion

This SLE-2 project demonstrates the implementation and performance analysis of BFS and DFS. In addition to measuring execution time and nodes expanded, the project uses cProfile and py-spy to collect profiling information and generate SVG flamegraph visualizations.

The project files, results, profiling outputs, and documentation are organized in the GitHub repository.
