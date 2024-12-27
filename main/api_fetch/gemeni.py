import diskcache
import google.generativeai as genai
from Secrets.load_env import GEMINI_API_KEY
from api_fetch.fetch_recipe import filter_out_avilable
import os 

cache_dir = "./cache"
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
cache = diskcache.Cache(cache_dir)

def send_message(food_items):
    if isinstance(food_items, tuple):
        food_items = [food_items]
    print(food_items)
    def format_responses(responses, missing_ingredients=None):
        formatted_responses = []

        for idx, recipe in enumerate(responses, 1):
            food_item_name = food_items[idx - 1][0] if isinstance(food_items[idx - 1], tuple) else food_items[idx - 1]
            formatted_response = f"**{food_item_name}**\n\n"
            formatted_response += recipe.replace("\n", "\n  ")
            
            # Add missing ingredients if available
            if missing_ingredients and idx <= len(missing_ingredients):
                missing = missing_ingredients[idx - 1]
                if missing:
                    formatted_response += f"\n\n \t Missing ingredients: {', '.join(missing)}\n\n\n"
            
            formatted_responses.append(formatted_response)

        return "\n\n".join(formatted_responses)

    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    responses = []
    missing_ingredients_list = []  

    for food_item in food_items:
        if isinstance(food_item, tuple):
            item_name = food_item[0]
            missing_ingredients = food_item[1]
        else:
            item_name = food_item
            missing_ingredients = None

        # Add missing ingredients to the list for formatting later
        missing_ingredients_list.append(missing_ingredients)
        item_ = item_name.split(" ")[0]
        cache_key = f"recipe_{item_}"

        if cache_key in cache:
            # Use cached response
            response = cache.get(cache_key)
        else:
            fetch = filter_out_avilable(item_)
            filtered = None
            if fetch:
                filtered = fetch[:2]

            prompt = f"Cook AI: Provide a small cooking guide for {item_name}, i will provide something i know if it feels vague or lacks info please ignore it."
            if filtered:
                prompt += f" using {', '.join(filtered)}."
            prompt += " Be clear and concise, assuming the user is a beginner. Just tell me the instructions, nothing else. Keep it as short as possible and avoid unnecessary details. if there is any invalid information, please ignore it and give the proper recipe for food item."

            try:
                response_obj = model.generate_content(prompt)
                response = response_obj.text  # Extract the text from the response object
                cache.set(cache_key, response, expire=3600)  # Cache the response for 1 hour
            except Exception as e:
                print(f"An error occurred for item '{item_name}': {e}")
                response = None

        responses.append(response if response else None)

    return format_responses(responses, missing_ingredients_list)
