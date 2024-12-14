import heapq

def find_recipes_dijkstra(graph, diet_preference, available_ingredients):
    bestrecipes = []
    betterrecipes = []

    p_queue = []
    
    for item in graph.nodes:
        if graph.nodes[item]["type"] == "recipe":
            weight, missing_ingredients = calculate_weight(graph, item, diet_preference, available_ingredients)
            
            if weight == 0:
                bestrecipes.append(item)
            
            else:
                heapq.heappush(p_queue, (weight, item, missing_ingredients))
    
    if p_queue:
        while p_queue:
            weight, recipe, missing_ingredients = heapq.heappop(p_queue)
            if weight <= 3:  
                betterrecipes.append((recipe, missing_ingredients))
    
    if bestrecipes:
        return bestrecipes
    elif betterrecipes:
        return betterrecipes
    else:
        return []

# helper function to calculate the weight of each recipe on the basis of its dietary preference and ingredient availability
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
