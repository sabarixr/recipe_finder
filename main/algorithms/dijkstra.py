import heapq


def find_recipes_dijkstra(graph, diet_preference, available_ingredients):
    recipes_ingredients_returned = []  
    p_queue = []
    visited = set()  
    added_recipes = set()  

    for ingredient in available_ingredients:
        if ingredient not in visited:
            visited.add(ingredient)
            for neighbor in graph.neighbors(ingredient):
                if graph.nodes[neighbor]["type"] == "recipe":
                    weight, missing_ingredients = calculate_weight(graph, neighbor, diet_preference, available_ingredients)

                    if weight == 0 and neighbor not in added_recipes:
                        recipes_ingredients_returned.append((neighbor, []))  
                        added_recipes.add(neighbor)
                    elif neighbor not in added_recipes:
                        heapq.heappush(p_queue, (weight, neighbor, missing_ingredients))
                elif neighbor not in visited:
                    visited.add(neighbor)

    # Process recipes from the priority queue (better recipes with missing ingredients)
    while p_queue:
        weight, recipe, missing_ingredients = heapq.heappop(p_queue)
        if weight <= 3 and recipe not in added_recipes:  
            recipes_ingredients_returned.append((recipe, missing_ingredients))
            added_recipes.add(recipe)

    if recipes_ingredients_returned:
        print("Recipe(s) found according to your preferences and available ingredients")
        return recipes_ingredients_returned
    else:
        print("No recipes matching your preferences")
        return []

# Helper function to calculate the weight of each recipe based on dietary preference and ingredient availability
def calculate_weight(graph, recipe, diet_preference, available_ingredients):
    weight = 0
    missing_ingredients = []

    dietary_preference_list = graph.nodes[recipe].get("dietary_compatibility", [])
    if diet_preference not in dietary_preference_list:
        weight += 10  # Add weight if the recipe doesn't match the dietary preference

    for ingredient in graph.neighbors(recipe):
        if ingredient not in available_ingredients:
            weight += 1  # Add weight for each missing ingredient
            missing_ingredients.append(ingredient)

    # Remove duplicates from the missing ingredients
    missing_ingredients = list(set(missing_ingredients))

    return weight, missing_ingredients

