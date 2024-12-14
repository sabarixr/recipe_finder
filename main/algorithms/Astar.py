def find_recipes_a_star(graph, available_ingredients, time_limit, fastest=False):
    """
    A* search to find recipes that can be made with the available ingredients.

    :param graph: A networkx graph containing recipes and their ingredients.
    :param available_ingredients: A list of ingredients available to the user.
    :param time_limit: The maximum allowed preparation time.
    :param fastest: If True, return the single fastest recipe. If False, return all recipes within the time limit.
    :return: A tuple (recipe_name, missing_ingredients) if fastest=True, otherwise a list of recipes.
    """
    
    results = []
    best_recipe = None
    best_missing_ingredients = None
    best_prep_time = float('inf')
    best_match_count = -1  # Track the recipe with the most matching ingredients

    for node in graph.nodes:
        # Only consider nodes that represent recipes
        if graph.nodes[node].get("type") == "recipe":
            recipe_name = node
            recipe_data = graph.nodes[node]
            recipe_ingredients = set(recipe_data["ingredients"])
            prep_time = recipe_data["prep_time"]

            # Skip recipes that exceed the time limit
            if prep_time > time_limit:
                continue

            # Calculate matching ingredients and missing ingredients
            common_ingredients = recipe_ingredients & set(available_ingredients)
            match_count = len(common_ingredients)
            missing_ingredients = recipe_ingredients - set(available_ingredients)

            # Ensure recipes have enough matches to be considered feasible
            if match_count == 0 or match_count < len(recipe_ingredients) // 2:
                continue  # Skip recipes with less than half of their ingredients matched

            # Collect all valid recipes when fastest=False
            if not fastest:
                results.append((recipe_name, list(missing_ingredients), prep_time, match_count))

            # When fastest=True, find the single best recipe
            if fastest:
                if match_count > best_match_count or (match_count == best_match_count and prep_time < best_prep_time):
                    best_recipe = recipe_name
                    best_missing_ingredients = list(missing_ingredients)
                    best_prep_time = prep_time
                    best_match_count = match_count

    if fastest:
        if best_recipe:
            return best_recipe, best_missing_ingredients
        return "No valid recipe can be made with the given ingredients."

    # Sort results by heuristic: more matches first, then less prep time
    results.sort(key=lambda x: (-x[3], x[2]))  # Sort by match_count (desc) and prep_time (asc)
    return [(recipe, missing_ingredients) for recipe, missing_ingredients, _, _ in results]