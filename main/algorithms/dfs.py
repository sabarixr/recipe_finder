from algorithms.bfs import find_recipes_bfs


def find_recipes_dfs(graph, available_ingredients):
    visited = set()
    recipes_found = []
    print(available_ingredients)
    
    # Use BFS to find recipes with ≤ 2 missing ingredients
    bfs_data = find_recipes_bfs(graph, available_ingredients)
    if bfs_data:
        print(bfs_data)
        return bfs_data  # Return BFS results directly
    else:
        print("No BFS recipes found")

    # Define the DFS function
    def dfs(node):
        if node in visited:
            return
        visited.add(node)

        if graph.nodes[node]["type"] == "recipe":
            required_ingredients = set(graph.neighbors(node))
            missing_ingredients = required_ingredients - set(available_ingredients)
            if len(missing_ingredients) <= 2:
                recipes_found.append((node, list(missing_ingredients)))

        for neighbor in graph.neighbors(node):
            dfs(neighbor)

    # Start DFS from available ingredients
    for ingredient in available_ingredients:
        dfs(ingredient)
    
    return recipes_found
