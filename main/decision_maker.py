from numpy.testing.print_coercion_tables import print_cancast_table

from algorithms import dfs, Astar, dijkstra, bfs
from api_fetch.gemeni import send_message
from nlp.agent_txt import extract_ingredients

def get_response(Graph ,user_message, dietary, time_entry, cuisines):
    ingredients = list(extract_ingredients(user_message)) 
    if not ingredients:
        return "I am sorry, I can only help you cook if you provide ingredients."
    
    if ingredients:
        print(ingredients)
        if (dietary and time_entry and cuisines) or (dietary and time_entry) or (dietary and cuisines) or (time_entry and cuisines):
            return "The combined search feature is coming soon. Stay tuned!"


        
        if not (dietary or time_entry or cuisines):
            print("bfs/dfs")
            dfs_or_bfs_res = dfs.find_recipes_dfs(Graph, ingredients)
            if dfs_or_bfs_res:
                return send_message(dfs_or_bfs_res)
            else:
                return "Sorry but there was no recipes that can be cooked with the ingredients provided."
        if dietary:
            print("dia")
            return None
            # return dijkstra.find_recipes_dijkstra()
        if time_entry:
            print("time")
            return send_message(Astar.find_recipes_a_star(Graph, ingredients, time_entry, True))
        if cuisines:
            print("cus")
            return send_message(bfs.find_recipes_bfs(Graph, ingredients))

    return "Please provide additional preferences for dietary, time, or cuisines."
