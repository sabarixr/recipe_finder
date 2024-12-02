import networkx as nx

# Initialize the graph
G = nx.Graph()

# Data for the graph
ingredients = [
    "Egg", "Milk", "Flour", "Sugar", "Butter", "Banana", "Chicken", "Rice", "Tomato", "Onion", 
    "Garlic", "Cheese", "Spinach", "Carrot", "Potato", "Beef", "Fish", "Salt", "Pepper", "Oil",
    "Lettuce", "Bread", "Corn", "Pasta", "Basil", "Oregano", "Chili", "Honey", "Yogurt", "Cream",
    "Cucumber", "Mushroom", "Lemon", "Vinegar", "Ginger", "Soy Sauce", "Tofu", "Cabbage", "Beans", "Peas"
]

recipes = {
    "Pancake": {
        "ingredients": ["Egg", "Milk", "Flour", "Sugar", "Butter"],
        "difficulty": 2,
        "prep_time": 15,
        "dietary_weight": 3
    },
    "Omelette": {
        "ingredients": ["Egg", "Cheese", "Onion", "Salt", "Pepper"],
        "difficulty": 1,
        "prep_time": 10,
        "dietary_weight": 4
    },
    "Smoothie": {
        "ingredients": ["Milk", "Banana", "Honey", "Yogurt"],
        "difficulty": 1,
        "prep_time": 5,
        "dietary_weight": 3
    },
    "Cake": {
        "ingredients": ["Egg", "Milk", "Flour", "Sugar", "Butter"],
        "difficulty": 4,
        "prep_time": 60,
        "dietary_weight": 2
    },
    "Chicken Curry": {
        "ingredients": ["Chicken", "Tomato", "Onion", "Garlic", "Oil"],
        "difficulty": 3,
        "prep_time": 40,
        "dietary_weight": 5
    }
    # Add additional recipes here...
}

# Add nodes and edges to the graph
for ingredient in ingredients:
    G.add_node(ingredient, bipartite=0, type="ingredient")

for recipe, attributes in recipes.items():
    G.add_node(recipe, bipartite=1, type="recipe", **attributes)
    for ingredient in attributes["ingredients"]:
        G.add_edge(ingredient, recipe)

# Function to find recipes using BFS
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


def find_recipes_a_star(graph, available_ingredients, time_limit, fastest=False):
    def heuristic(node):
        # Use difficulty as a heuristic estimate (lower is better)
        return graph.nodes[node].get("difficulty", 0)

    open_set = set()
    g_score = {node: float('inf') for node in graph.nodes}
    f_score = {node: float('inf') for node in graph.nodes}

    # Initialize with available ingredients
    for ingredient in available_ingredients:
        g_score[ingredient] = 0
        f_score[ingredient] = heuristic(ingredient)
        open_set.add(ingredient)

    came_from = {}
    valid_recipes = []

    while open_set:
        # Pick the node with the lowest f_score
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

# Dijkstra's algorithm for recipes based on dietary preferences
def find_recipes_dijkstra(graph, start_ingredient):
    return nx.single_source_dijkstra_path(graph, start_ingredient, weight="dietary_weight")

# Example usage
available_ingredients = ["Milk", "Banana", "Honey", "Yogurt"]
print("Recipes (BFS):", find_recipes_bfs(G, available_ingredients))
print("Recipes (DFS):", find_recipes_dfs(G, available_ingredients))
print("Recipes (Dijkstra):", find_recipes_dijkstra(G, "Egg"))

available_ingredients = ["Egg", "Milk"]
time_limit = 20
fastest = True

print("Recipes (A* - Fastest):", find_recipes_a_star(G, available_ingredients, time_limit, fastest=True))
print("Recipes (A* - All within time):", find_recipes_a_star(G, available_ingredients, time_limit, fastest=False))

