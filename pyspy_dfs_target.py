import time
from graph_data import graph
from sle2_profiling import dfs

def run_dfs():
    end_time = time.time() + 15
    while time.time() < end_time:
        dfs(graph, "A", "G")

if __name__ == "__main__":
    run_dfs()
