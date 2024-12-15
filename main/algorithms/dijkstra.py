import networkx as nx
import heapq

def find_recipes_dijkstra(graph, diet_preference, available_ingredients):
    bestrecipes = []
    betterrecipes = {}
    p_queue = []
    visited = set()  

    for ingredient in available_ingredients:
        if ingredient not in visited:
            visited.add(ingredient)
            for neighbor in graph.neighbors(ingredient):
                if graph.nodes[neighbor]["type"] == "recipe":
                    weight, missing_ingredients = calculate_weight(
                        graph, neighbor, diet_preference, available_ingredients
                    )

                    if weight == 0:
                        bestrecipes.append(neighbor)
                    else:
                        heapq.heappush(p_queue, (weight, neighbor, missing_ingredients))
                elif neighbor not in visited:
                    visited.add(neighbor)

  
    if p_queue:
        while p_queue:
            weight, recipe, missing_ingredients = heapq.heappop(p_queue)
            if weight <= 3:  
                betterrecipes[recipe] = missing_ingredients

    
    if bestrecipes:
        print("Recipe(s) found according to your preferences and available ingredients")
        return bestrecipes
    elif betterrecipes:
        print("Recipe(s) found according to your preferences with a few ingredients missing (up to 3)")
        return betterrecipes
    else:
        print("No recipes matching your preferences")
        return {}

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

    return weight, missing_ingredients
