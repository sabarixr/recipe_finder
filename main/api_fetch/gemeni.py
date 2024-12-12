import google.generativeai as genai
from Secrets.load_env import GEMINI_API_KEY
from api_fetch.fetch_recipe import filter_out_avilable

def send_message(food_items):
    def format_responses(responses):
        formatted_responses = []

        for idx, recipe in enumerate(responses, 1):
            food_item_name = food_items[idx - 1]
            formatted_response = f"**{food_item_name}**\n"
            formatted_response += recipe.replace("\n", "\n  ")  
            formatted_responses.append(formatted_response)

        return "\n\n".join(formatted_responses)
    

    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    responses = []
    
    for food_item in food_items:
        item_ = food_item.split(" ")[0]
        filtered = filter_out_avilable(item_)[:2]

        prompt = f"Cook AI: Provide a small cooking guide for {food_item}"
        if filtered:
            prompt += f" using {', '.join(filtered)}."
        prompt += " Be clear and concise, assuming the user is a beginner. Just tell me the instructions, nothing else. Keep it as short as possible and avoid unnecessary details."

        try:
            response = model.generate_content(prompt)
            responses.append(response.text)
        except Exception as e:
            print(f"An error occurred for item '{food_item}': {e}")
            responses.append(None)


    return format_responses(responses)
