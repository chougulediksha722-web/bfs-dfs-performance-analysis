from collections import deque


def bfs(graph, start, target):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node == target:
            return True

        if node in visited:
            continue

        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return False