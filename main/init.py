import networkx as nx

def create_recipe_graph():
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

    return G
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


gemini = genai.GenerativeModel(
    model_name="gemini-pro",
)

def send_message(food_item_with_ingredients):
    try:
        ai_identity_context = (
            "Cook AI: Provide a detailed cooking guide for the given food item. "
            "Only give response based on the ingredients given."
            "Speak as if you're guiding someone new to cooking."
        )
        chat = gemini.start_chat()
        message_with_context = ai_identity_context + " User asked: " + food_item_with_ingredients
        response = chat.send_message(message_with_context)

        return response.text  
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


