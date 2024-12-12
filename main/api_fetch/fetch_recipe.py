import requests
from bs4 import BeautifulSoup

from Secrets.load_env import SPOONACULAR_API_KEY
from algorithms.decision_tree_simple_mcdm import combine_data_using_decision_tree





def get_recipe_details_spoonacular(food_name):
    # Construct the search URL
    food_search_url = f"https://api.spoonacular.com/recipes/complexSearch?query={food_name}&addRecipeInformation=true&apiKey={SPOONACULAR_API_KEY}"
    
    # Perform the search request
    response = requests.get(food_search_url)
    if response.status_code == 200:
        results = response.json().get('results', [])
        if results:
            recipe = results[0]  
            id = recipe['id']
            title = recipe['title']
            summary = recipe['summary']
            fetch = BeautifulSoup(summary, "html.parser")
            summary = fetch.get_text().split("It is brought to you by")[0]
            rec_url = f"https://api.spoonacular.com/recipes/{id}/card?apiKey={SPOONACULAR_API_KEY}"
            response = requests.get(rec_url)
            if response.status_code == 200:
                img_link = response.json().get('url')
                return title, summary, img_link
    return None

def get_meal_details_meal_db(food_name):
    meal_search_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={food_name}"
    response = requests.get(meal_search_url)
    if response.status_code == 200:
        meals = response.json().get('meals', [])
        if meals:
            meal = meals[0] 
            meal_name = meal['strMeal']
            instructions = meal['strInstructions']
            meal_thumb = meal['strMealThumb']
            return meal_name, instructions, meal_thumb
    return None


def filter_out_avilable(food_item):
    spoonacular = get_recipe_details_spoonacular(food_item)
    meal_db = get_meal_details_meal_db(food_item)
    if spoonacular and meal_db:
        title, summary, image = combine_data_using_decision_tree(spoonacular, meal_db)
        return title, summary, image
    elif spoonacular:
        return spoonacular
    elif meal_db:
        return meal_db
    else:
        return None


