def dfs(graph, start, target, visited=None):
    if visited is None:
        visited = set()

    if start == target:
        return True

    if start in visited:
        return False

    visited.add(start)

    for neighbor in graph.get(start, []):
        if dfs(graph, neighbor, target, visited):
            return True

    return False
