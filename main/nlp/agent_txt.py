import spacy
from data import get_ingredients
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

try:
    nlp = spacy.load("en_core_web_sm")
except OSError as e:
    raise RuntimeError("Could not load spacy model 'en_core_web_sm' is it is installed.") from e



original_ingredient_list = get_ingredients()
normalized_ingredient_list = {item.lower(): item for item in original_ingredient_list} 


def normalize_ingredient(ingredient, normalized_list, threshold=85):
    try:
        match = process.extractOne(ingredient, normalized_list.keys(), scorer=fuzz.ratio)
        if match and match[1] >= threshold:
            return normalized_list[match[0]]
    except Exception as e:
        print(f"Error during ingredient normalization: {e}")
    return None

def extract_ingredients(user_input):
    doc = nlp(user_input)
    extracted_ingredients = set()

    for chunk in doc.noun_chunks:
        try:
            ingredient_text = chunk.text.lower()
            ingredient_lemma = " ".join([token.lemma_ for token in nlp(ingredient_text)])  # lematize the ingredient text
        except Exception as e:
            print(f"Error processing chunk '{chunk.text}': {e}")
            continue
       
        normalized = normalize_ingredient(ingredient_lemma, normalized_ingredient_list)
        if normalized:
            extracted_ingredients.add(normalized)
        else:
            for word in ingredient_text.split():
                singular_word = word.rstrip('s') 
                if singular_word in normalized_ingredient_list:
                    extracted_ingredients.add(normalized_ingredient_list[singular_word])
    
    return extracted_ingredients

