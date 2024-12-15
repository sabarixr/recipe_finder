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

    visited_recipes = set()  # To avoid revisiting recipes

    for ingredient in available_ingredients:
        # Check if the ingredient is in the graph and is marked as an ingredient node
        if ingredient in graph.nodes and graph.nodes[ingredient].get("type") == "ingredient":
            for neighbor in graph.neighbors(ingredient):
                # Skip already visited recipes
                if neighbor in visited_recipes:
                    continue
                # Ensure the neighbor is a recipe
                if graph.nodes[neighbor].get("type") == "recipe":
                    visited_recipes.add(neighbor)

                    # Get recipe data
                    recipe_name = neighbor
                    recipe_data = graph.nodes[recipe_name]
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
                    if len(recipe_ingredients) - match_count > 2:
                        continue 

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
    
    # If fastest is True, return the best recipe found
    if fastest:
        if best_recipe:
            return [(best_recipe, best_missing_ingredients)]
        return None  # Explicitly return None if no recipe matches

    # If no valid recipes were found
    if not results:
        return None

    # Sort results by match_count (desc) and prep_time (asc)
    results.sort(key=lambda x: (-x[3], x[2]))  # Sort by match_count (desc) and prep_time (asc)

    # Use a for loop to return the results
    final_results = []
    for recipe, missing_ingredients, _, _ in results:
        final_results.append((recipe, missing_ingredients))

    return final_results