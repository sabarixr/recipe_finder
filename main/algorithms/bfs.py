def find_recipes_bfs(graph, available_ingredients, cuisine=None):
    visited = set()  
    queue = []  
    for ingredient in available_ingredients:
        queue.append(ingredient)  

    recipes_found = []  

    while len(queue) > 0:  
        current = queue.pop(0)  
        if current in visited:
            continue  
        visited.add(current)  
        for neighbor in graph.neighbors(current):
            
            if graph.nodes[neighbor]["type"] == "recipe":
                
                if cuisine is not None:
                    recipe_cuisine = graph.nodes[neighbor].get("cuisine", None)
                    if recipe_cuisine != cuisine:
                        continue  
                
                
                required_ingredients = set(graph.neighbors(neighbor))
                if required_ingredients.issubset(set(available_ingredients)):  
                    if neighbor not in recipes_found:
                        recipes_found.append(neighbor)
            elif neighbor not in visited:
                queue.append(neighbor)  

    return recipes_found
