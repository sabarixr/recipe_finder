import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()  
api_key = os.environ["API_KEY"]

example_food = "banana smoothie"
food_search_url = f"https://api.spoonacular.com/recipes/complexSearch?query={example_food}&addRecipeInformation=true&apiKey={api_key}"

response = requests.get(food_search_url)

if response.status_code == 200:
    results = response.json().get('results', [])
    if results:
        recipe = results[0]  
        id = recipe['id']
        title = recipe['title']
        summary = recipe['summary']
        image_url = recipe['image']
        soup = BeautifulSoup(summary, "html.parser")
        summary = soup.get_text()
        summary = summary.split("It is brought to you by")[0] 
        print("Recipe ID:",id)
        print("Title: ",title)
        print("Summary:",summary)
    else:
        print("No results found for the food item.")
recipe_url=f"https://api.spoonacular.com/recipes/{id}//card?apiKey={api_key}"
response=requests.get(recipe_url)
if response.status_code==200:
    image=response.json()['url']
    print(image)