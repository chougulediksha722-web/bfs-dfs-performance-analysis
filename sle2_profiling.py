from collections import deque
import time


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}


def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    nodes = 0

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes += 1

        if node == goal:
            return nodes

        for neighbour in graph[node]:
            queue.append(neighbour)

    return nodes


def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes += 1

        if node == goal:
            return nodes

        for neighbour in graph[node]:
            stack.append(neighbour)

    return nodes


def measure(algorithm, name):
    runs = 10000

    start_time = time.perf_counter()

    for _ in range(runs):
        algorithm(graph, "A", "G")

    end_time = time.perf_counter()

    total_time = (end_time - start_time) * 1000
    nodes = algorithm(graph, "A", "G")

    print(name)
    print(f"Total time: {total_time:.6f} ms")
    print(f"Nodes expanded: {nodes}")
    print()


if __name__ == "__main__":
    measure(bfs, "BFS")
    measure(dfs, "DFS")