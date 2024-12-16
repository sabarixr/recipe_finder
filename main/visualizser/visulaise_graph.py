from matplotlib import pyplot as plt
import networkx as nx

def visualize_graph(graph):
    plt.figure(figsize=(50,250))  

    # Use bipartite layout for proper separation
    ingredients = [n for n, d in graph.nodes(data=True) if d.get('bipartite') == 0]
    recipes = [n for n, d in graph.nodes(data=True) if d.get('bipartite') == 1]
    pos = nx.bipartite_layout(graph, ingredients, align='vertical')
    
    # Adjust positions for better spacing
    ingredient_offset = 1 
    for i, node in enumerate(ingredients):
        x, y = pos[node]
        pos[node] = (x, y * ingredient_offset)  # Increase vertical spacing for ingredients

    
    for key, (x, y) in pos.items():
        pos[key] = (x * 2.5, y)  

    
    nx.draw_networkx_nodes(graph, pos, nodelist=ingredients, node_color="skyblue", label="Ingredients", node_size=900)
    nx.draw_networkx_nodes(graph, pos, nodelist=recipes, node_color="lightgreen", label="Recipes", node_size=700)
    nx.draw_networkx_edges(graph, pos, edge_color="gray", alpha=0.3)  
    nx.draw_networkx_labels(graph, pos, font_size=6, font_color="black") 

    plt.title("Recipe and Ingredient Bipartite Graph", fontsize=18)
    plt.legend(scatterpoints=1)
    plt.axis('off')
    plt.savefig("recipe_graph_bipartite_improved.png")
    print("Graph saved as 'recipe_graph_bipartite_improved.png'")