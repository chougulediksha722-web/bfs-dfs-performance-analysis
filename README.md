\# SLE-2: BFS vs DFS Profiling



A Python-based performance profiling project comparing Breadth-First Search (BFS) and Depth-First Search (DFS) on the same graph.



\## Objective



The objective of this project is to:



\- Implement BFS and DFS in Python.

\- Run both algorithms on the same graph.

\- Measure their execution time.

\- Compare the number of nodes expanded.

\- Profile the execution of the algorithms.

\- Analyse their performance.



\## Algorithms Used



\### Breadth-First Search (BFS)



BFS explores a graph level by level using a queue.



\### Depth-First Search (DFS)



DFS explores a graph by going deeper before backtracking, using a stack.



\## Technologies Used



\- Python

\- Git

\- GitHub

\- Visual Studio Code

\- GitHub Copilot

\- Python `timeit`

\- Python `cProfile`

\- Flameprof



\## Project Structure



\- `sle2\_profiling.py` - BFS and DFS implementation and performance measurement

\- `graph\_data.py` - Graph data used by the algorithms

\- `pyspy\_target.py` - Target program prepared for profiling

\- `profiling/` - Profiling output files

\- `results/results.txt` - Performance results

\- `report 1/` - SLE-2 project report

\- `CONTRIBUTION\_LOG.md` - AI contribution record

\- `.gitignore` - Ignores Python cache files



\## Performance Results



The algorithms were executed 10,000 times for timing measurement.



| Algorithm | Nodes Expanded | Average Time for 10,000 Runs | Average Time per Run |

|-----------|----------------|-------------------------------|----------------------|

| BFS | 7 | 0.0095373 seconds | 0.00095373 ms |

| DFS | 3 | 0.0040775 seconds | 0.00040775 ms |



The measured execution times can vary depending on the computer and execution environment.



\## Profiling



The `profiling` folder contains the profiling outputs:



\- `bfs.prof`

\- `bfs\_profile.svg`

\- `dfs.prof`

\- `dfs\_profile.svg`



The profiling files were generated during the performance analysis and are included as project evidence.



\## How to Run



Open the project in Visual Studio Code or PowerShell.



Run:



```powershell

py -3.12 sle2\_profiling.py

