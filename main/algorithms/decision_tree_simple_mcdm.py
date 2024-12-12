
def combine_data_using_decision_tree(spoonacular_data,mealdb_data ):

    if not spoonacular_data and not mealdb_data:
        return None  
    spoonacular_title, spoonacular_summary, spoonacular_image = spoonacular_data if spoonacular_data else ('', '', '')
    mealdb_title, mealdb_summary, mealdb_image = mealdb_data if mealdb_data else ('', '', '')

    if spoonacular_summary and len(spoonacular_summary) > 50:
        summary = spoonacular_summary
    elif mealdb_summary and len(mealdb_summary) > 50:
        summary = mealdb_summary
    else:
        summary = spoonacular_summary if spoonacular_summary else mealdb_summary

    if spoonacular_title and len(spoonacular_title) > len(mealdb_title):
        title = spoonacular_title
    else:
        title = mealdb_title


    if mealdb_image and mealdb_image != '':
        image = mealdb_image
    elif spoonacular_image and spoonacular_image != '' != '':
        image = spoonacular_image
    else:
        image = None 

    return title, summary, image
