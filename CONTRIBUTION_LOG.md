SLE-2 – Contribution Log

Project Information

Project Name: SLE-2 – BFS & DFS Performance Analysis
Developer: Diksha Chougule
GitHub Username: chougulediksha722-web
GitHub Repository: bfs-dfs-performance-analysis
AI Coding Tool: GitHub Copilot
Programming Language: Python



Project Description

This project analyzes and compares the performance of two fundamental graph traversal algorithms:

* Breadth-First Search (BFS)
* Depth-First Search (DFS)

The project measures execution time and the number of nodes expanded by each algorithm. Profiling tools are also used to analyze the execution of the algorithms and generate visual profiling outputs.



Contribution / Development Log

1. Project Setup

Created the SLE-2 project repository and established the basic project structure for BFS and DFS performance analysis.

The project contains Python source files, profiling outputs, result files, and documentation.



2. Graph Data Creation

Created graph_data.py to store the graph used for testing the BFS and DFS algorithms.

The graph provides a common input so that both algorithms can be executed and compared under the same conditions.



3. BFS and DFS Implementation

Implemented BFS and DFS traversal functions in sle2_profiling.py.

The algorithms were executed using the same graph and the same start and goal nodes so their performance could be compared.



4. Performance Measurement

Added execution-time measurement and node-expansion counting for both algorithms.

Example execution output:

BFS
Total time: 9.205100 ms
Nodes expanded: 7
DFS
Total time: 4.285200 ms
Nodes expanded: 3

The measured values can vary slightly between executions because execution time depends on the system and runtime conditions.



5. cProfile Profiling

Used Python’s built-in cProfile module to profile the BFS and DFS executions.

Separate profiling scripts were created to run the algorithms repeatedly and generate profiling data:

* profile_bfs.py
* profile_dfs.py

Profiling data was saved as:

* profiling/bfs_clean.prof
* profiling/dfs_clean.prof

Flamegraph-style SVG outputs were generated from the profiling data.



6. py-spy Profiling

After cProfile profiling, py-spy was used to perform sampling-based runtime profiling.

Separate target programs were created for BFS and DFS:

* pyspy_bfs_target.py
* pyspy_dfs_target.py

The programs repeatedly execute the corresponding algorithm so that py-spy can collect enough samples.

The profiling results were generated as SVG flamegraphs:

* profiling/pyspy_bfs.svg
* profiling/pyspy_dfs.svg

The Python 3.14 executable was used with py-spy to avoid the Python-version detection issue encountered earlier.



7. Profiling Visualization

The generated SVG flamegraphs provide a visual representation of where execution time is spent during BFS and DFS execution.

The profiling outputs are stored inside the profiling/ directory.



8. Results Documentation

The measured BFS and DFS performance results were recorded in:

results/results.txt

The results include:

 Total execution time
 Number of nodes expanded



9. Project Documentation

Updated README.md with:

* Project overview
* BFS and DFS description
* Project structure
* Execution instructions
* Performance results
* cProfile profiling information
* py-spy profiling information
* Generated SVG profiling outputs

⸻

10. Git and GitHub

The project files were added and committed to Git.

The documentation and project updates were pushed to the GitHub repository.

The repository is:

bfs-dfs-performance-analysis

The final working tree was verified using:

git status

and confirmed clean after committing and pushing the changes.



Final Project Structure

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

⸻

Tools Used

* Python – Algorithm implementation and execution
* Git & GitHub – Version control and project hosting
* GitHub Copilot – AI coding assistance
* cProfile – Python performance profiling
* flameprof – Generation of flamegraph-style visualization from cProfile data
* py-spy – Sampling-based Python profiling
* SVG – Profiling visualization format

⸻

Conclusion

The SLE-2 project successfully implements BFS and DFS and compares their execution performance using execution-time and node-expansion measurements.

The project was further enhanced using both cProfile and py-spy to provide profiling data and visual flamegraph outputs. The results and profiling files are organized in the repository along with the project documentation.
