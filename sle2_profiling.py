from collections import deque
import timeit

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


def measure(algorithm, name):
    times = timeit.repeat(
        lambda: algorithm(graph, "A", "G"),
        repeat=3,
        number=10000
    )

    average_time = sum(times) / len(times)
    average_per_run = (average_time / 10000) * 1000
    nodes = algorithm(graph, "A", "G")

    print(name)
    print("Nodes Expanded:", nodes)
    print("Average Time for 10000 runs:", average_time, "seconds")
    print("Average Time per run:", average_per_run, "ms")
    print()


if __name__ == "__main__":
    measure(bfs, "BFS")
    measure(dfs, "DFS")