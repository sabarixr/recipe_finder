def find_recipes_a_star(graph, available_ingredients, time_limit, fastest=False):  
    results = []
    best_recipe = None
    best_missing_ingredients = None
    best_prep_time = float('inf')
    best_match_count = -1  

    visited_recipes = set()  

    for ingredient in available_ingredients:
        
        if ingredient in graph.nodes and graph.nodes[ingredient].get("type") == "ingredient":
            for neighbor in graph.neighbors(ingredient):
                
                if neighbor in visited_recipes:
                    continue
                
                if graph.nodes[neighbor].get("type") == "recipe":
                    visited_recipes.add(neighbor)

                    
                    recipe_name = neighbor
                    recipe_data = graph.nodes[recipe_name]
                    recipe_ingredients = set(recipe_data["ingredients"])
                    prep_time = recipe_data["prep_time"]

                    
                    if prep_time > time_limit:
                        continue

                    
                    common_ingredients = recipe_ingredients & set(available_ingredients)
                    match_count = len(common_ingredients)
                    missing_ingredients = recipe_ingredients - set(available_ingredients)

                    
                    if len(recipe_ingredients) - match_count > 2:
                        continue 

                    
                    if not fastest:
                        results.append((recipe_name, list(missing_ingredients), prep_time, match_count))

                    
                    if fastest:
                        if match_count > best_match_count or (match_count == best_match_count and prep_time < best_prep_time):
                            best_recipe = recipe_name
                            best_missing_ingredients = list(missing_ingredients)
                            best_prep_time = prep_time
                            best_match_count = match_count
    
    
    if fastest:
        if best_recipe:
            return [(best_recipe, best_missing_ingredients)]
        return None  

    
    if not results:
        return None

    
    results.sort(key=lambda x: (-x[3], x[2]))  

    
    final_results = []
    for recipe, missing_ingredients, _, _ in results:
        final_results.append((recipe, missing_ingredients))

    return final_results