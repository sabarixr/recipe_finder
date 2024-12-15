from matplotlib import pyplot as plt
import networkx as nx

def visualize_graph(graph):
    plt.figure(figsize=(20, 32))  # Larger figure for more spacing

    # Use bipartite layout for proper separation
    ingredients = [n for n, d in graph.nodes(data=True) if d.get('bipartite') == 0]
    recipes = [n for n, d in graph.nodes(data=True) if d.get('bipartite') == 1]
    pos = nx.bipartite_layout(graph, ingredients, align='vertical')
    
    # Adjust positions for better spacing
    ingredient_offset = 3  # Vertical spacing multiplier for ingredients
    for i, node in enumerate(ingredients):
        x, y = pos[node]
        pos[node] = (x, y * ingredient_offset)  # Increase vertical spacing for ingredients

    # Offset for better horizontal spacing for both node types
    for key, (x, y) in pos.items():
        pos[key] = (x * 1.2, y)

    # Draw nodes and edges with customization
    nx.draw_networkx_nodes(graph, pos, nodelist=ingredients, node_color="skyblue", label="Ingredients", node_size=1300)
    nx.draw_networkx_nodes(graph, pos, nodelist=recipes, node_color="lightgreen", label="Recipes", node_size=1000)
    nx.draw_networkx_edges(graph, pos, edge_color="gray", alpha=0.5)
    nx.draw_networkx_labels(graph, pos, font_size=8, font_color="black")

    plt.title("Recipe and Ingredient Bipartite Graph", fontsize=16)
    plt.legend(scatterpoints=1)
    plt.axis('off')
    plt.savefig("recipe_graph_bipartite.png")
    print("Graph saved as 'recipe_graph_bipartite.png'")
