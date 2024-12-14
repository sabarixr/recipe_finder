from numpy.testing.print_coercion_tables import print_cancast_table

from algorithms import dfs, Astar, dijkstra, bfs
from api_fetch.gemeni import send_message
from nlp.agent_txt import extract_ingredients

def get_response(Graph ,user_message, dietary, time_entry, cuisines, fastest= False):
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
            print("dijkstra")
            return_data = dijkstra.find_recipes_dijkstra(Graph, dietary, ingredients)
            if return_data:
                print(return_data)
                return send_message(return_data)
            else:
                return "Sorry but there was no recipes that can be cooked with the ingredients provided."

        if time_entry:
            print("A* time")
            return_data = Astar.find_recipes_a_star(Graph, ingredients, int(time_entry), fastest)
            if return_data:
                print(return_data)
                return send_message(return_data)
            else:
                return "Sorry but there was no recipes that can be cooked with the ingredients provided."
        if cuisines:
            print("cus")
            bfs_data = bfs.find_recipes_bfs(Graph, ingredients,cuisines)
            if bfs_data:
                print(bfs_data)
                return send_message(bfs_data)
            else:
                return "Sorry but there was no recipes that can be cooked with the ingredients provided."
    return "Please provide additional preferences for dietary, time, or cuisines."
