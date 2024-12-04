
def find_recipes_a_star(graph, available_ingredients, time_limit, fastest=False):
    def heuristic(node):
        return graph.nodes[node].get("difficulty", 0)

    open_set = set()
    g_score = {node: float('inf') for node in graph.nodes}
    f_score = {node: float('inf') for node in graph.nodes}
    for ingredient in available_ingredients:
        g_score[ingredient] = 0
        f_score[ingredient] = heuristic(ingredient)
        open_set.add(ingredient)

    came_from = {}
    valid_recipes = []

    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        open_set.remove(current)

        if graph.nodes[current]["type"] == "recipe":
            prep_time = graph.nodes[current]["prep_time"]
            if prep_time <= time_limit:
                valid_recipes.append((current, prep_time, graph.nodes[current]["difficulty"]))

        for neighbor in graph.neighbors(current):
            tentative_g_score = g_score[current] + graph.nodes.get(current, {}).get("prep_time", 1)
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor)
                open_set.add(neighbor)

    if fastest:
        return min(valid_recipes, key=lambda x: (x[1], x[2]))[0] if valid_recipes else None
    else:
        return [recipe[0] for recipe in valid_recipes]
