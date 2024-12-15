from algorithms.bfs import find_recipes_bfs

def find_recipes_dfs(graph, available_ingredients):
    visited = set()
    recipes_found = []
    print(available_ingredients)
    
    # Call BFS first to get preliminary recipe suggestions
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

        # Correctly access 'type' attribute
        node_type = graph.nodes[node].get("type")
        if node_type == "recipe":
            required_ingredients = set(graph.neighbors(node))
            missing_ingredients = required_ingredients - set(available_ingredients)
            if len(missing_ingredients) <= 2:
                recipes_found.append((node, list(missing_ingredients)))

        for neighbor in graph.neighbors(node):
            dfs(neighbor)

    for ingredient in available_ingredients:
        dfs(ingredient)
    

    if not recipes_found:
        return None

    return recipes_found
