
def find_recipes_dfs(graph, available_ingredients):
    visited = set()
    recipes_found = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)

        if graph.nodes[node]["type"] == "recipe":
            required_ingredients = set(graph.neighbors(node))
            missing_ingredients = required_ingredients - set(available_ingredients)
            if len(missing_ingredients) <= 2:
                recipes_found.append(node)

        for neighbor in graph.neighbors(node):
            dfs(neighbor)

    for ingredient in available_ingredients:
        dfs(ingredient)

    return recipes_found