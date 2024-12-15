
# # # from algorithms.Astar import find_recipes_a_star

# # # # from algorithms.bfs import find_recipes_bfs
# # # # from algorithms.dfs import find_recipes_dfs
# # # # from algorithms.dijkstra import find_recipes_dijkstra
# # # from init import create_recipe_graph
# # # G = create_recipe_graph()
# # # # available_ingredients = ["Egg", "Milk", "Flour"]
# # # # print("Recipes (BFS):", find_recipes_bfs(G, available_ingredients))
# # # # print("Recipes (DFS):", find_recipes_dfs(G, available_ingredients))
# # # # print("Recipes (Dijkstra):", find_recipes_dijkstra(G,"gluten-free", ["Egg", "Milk", "Flour", "Sugar"]))

# # # available_ingredients = ["Egg", "Milk", "Flour", "Sugar", "Butter"]
# # # time_limit = 20
# # # fastest = True

# # # # print("Recipes (A* - Fastest):", find_recipes_a_star(G, available_ingredients, time_limit, fastest=True))
# # # print("Recipes (A* - All within time):", find_recipes_a_star(G, available_ingredients, time_limit, fastest=False))
# # # # #
# # # #
# # # # from nlp.speak_message import generate_audio
# # # #
# # # # generate_audio("Pasta")


# from algorithms.Astar import find_recipes_a_star
# # # # # from algorithms.bfs import find_recipes_bfs
# # # # from algorithms.dfs import find_recipes_dfs
# # # # # from algorithms.dijkstra import find_recipes_dijkstra

# from init import create_recipe_graph
# G = create_recipe_graph()
# # # # available_ingredients = ["Egg", "Milk", "Flour"]
# # # # # print("Recipes (BFS):", find_recipes_bfs(G, available_ingredients))
# # # # print("Recipes (DFS):", find_recipes_dfs(G, available_ingredients))
# # # # # # print("Recipes (Dijkstra):", find_recipes_dijkstra(G, "Egg"))

# available_ingredients = ["Egg", "Milk"]
# time_limit = 20
# fastest = True

# print("Recipes (A* - Fastest):", find_recipes_a_star(G, available_ingredients, time_limit, fastest=True))
# print("Recipes (A* - All within time):", find_recipes_a_star(G, available_ingredients, time_limit, fastest=False))

# # # #
# # # # from nlp.speak_message import generate_audio
# # # #
# # # # generate_audio("Pasta")


# # # from nlp.speak_message import generate_audio

# # # generate_audio("the sky is so cool to look at in the night")

# # import subprocess


# # args = [
# #     "mimic3",
# #     "\"Hello World\"",
# #     "--output-dir", "OUTPUT/DIR"]
# # try:
# #     subprocess.check_call(args)
# # except subprocess.CalledProcessError as e:
# #     # Handle error
# #     pass

# # from init import create_recipe_graph
# # import visualizser.visulaise_graph as visualizser


# # G = create_recipe_graph()
# # # visualize_graph(G)
# # visualizser.visualize_graph(G)
# # from algorithms.dfs import find_recipes_dfs
# # from init import create_recipe_graph
# # from api_fetch.gemeni import send_message

# # G = create_recipe_graph()
# # available_ingredients = ["Bread", "Cheese"]
# # dfs = find_recipes_dfs(G, available_ingredients)


# # print(send_message(dfs))
from algorithms.Astar import find_recipes_a_star
# from visualizser.visulaise_graph import visualize_graph
# from algorithms.bfs import find_recipes_bfs
# from algorithms.dfs import find_recipes_dfs
from algorithms.dijkstra import find_recipes_dijkstra
from init import create_recipe_graph
G = create_recipe_graph()
# available_ingredients = ["Egg", "Milk", "Flour"]
# print("Recipes (BFS):", find_recipes_bfs(G, available_ingredients))
# print("Recipes (DFS):", find_recipes_dfs(G, available_ingredients))
# print("Recipes (Dijkstra):", find_recipes_dijkstra(G,"gluten-free", ["Egg", "Milk", "Flour", "Sugar"]))

available_ingredients = ["Egg", "Milk", "Flour"]
time_limit = 20
fastest = True
# print(find_recipes_dijkstra(G,"low-carb",available_ingredients))
print("Recipes (A* - Fastest):", find_recipes_a_star(G, available_ingredients, time_limit, fastest=True))
print("Recipes (A* - All within time):", find_recipes_a_star(G, available_ingredients, time_limit, fastest=False))

#
# from nlp.speak_message import generate_audio
#
# generate_audio("Pasta")
# visualize_graph(G)