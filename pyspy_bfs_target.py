import time
from graph_data import graph
from sle2_profiling import bfs

def run_bfs():
    end_time = time.time() + 15
    while time.time() < end_time:
        bfs(graph, "A", "G")

if __name__ == "__main__":
    run_bfs()
