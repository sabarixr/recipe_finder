def find_recipes_bfs(graph, available_ingredients):
    visited = set()
    queue = list(available_ingredients)
    recipes_found = []

    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)

        for neighbor in graph.neighbors(current):
            if graph.nodes[neighbor]["type"] == "recipe":
                required_ingredients = set(graph.neighbors(neighbor))
                # Check if all required ingredients are in the available_ingredients
                if required_ingredients.issubset(available_ingredients):
                    if neighbor not in recipes_found:
                        recipes_found.append(neighbor)
            elif neighbor not in visited:
                queue.append(neighbor)

    return recipes_found


