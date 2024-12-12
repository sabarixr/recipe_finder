import networkx as nx

from data import get_ingredients, get_recipes

def create_recipe_graph():
    G = nx.Graph()

    ingredients = get_ingredients()
    recipes = get_recipes()

    for ingredient in ingredients:
        G.add_node(ingredient, bipartite=0, type="ingredient")

    for recipe, attributes in recipes.items():
        G.add_node(recipe, bipartite=1, type="recipe", **attributes)
        for ingredient in attributes["ingredients"]:
            G.add_edge(ingredient, recipe)

    return G

