import time

from graph_data import graph
from sle2_profiling import dfs

end_time = time.time() + 10

while time.time() < end_time:
    dfs(graph, "A", "G")