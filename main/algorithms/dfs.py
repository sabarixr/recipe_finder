from algorithms.bfs import find_recipes_bfs


def find_recipes_dfs(graph, available_ingredients):
    visited = set()
    recipes_found = []
    print(available_ingredients)
    bfs_data = find_recipes_bfs(graph, available_ingredients)
    if bfs_data:
        print(bfs_data)
        print("hi no hehe")
        return bfs_data
    else:
        print("no bfs found")

    def dfs(node):
        if node in visited:
            return
        visited.add(node)

        if graph.nodes[node]["type"] == "recipe":
            required_ingredients = set(graph.neighbors(node))
            missing_ingredients = required_ingredients - set(available_ingredients)
            if len(missing_ingredients) <= 2:
                print(missing_ingredients)
                recipes_found.append(node)

        for neighbor in graph.neighbors(node):
            dfs(neighbor)

    for ingredient in available_ingredients:
        dfs(ingredient)
    return recipes_found