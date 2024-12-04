
import time
import pyttsx3
import spacy
import  speech_recognition  as sr



nlp = spacy.load("en_core_web_sm")

# Predefined list of common ingredients
ingredient_list = [
    "egg", "milk", "flour", "butter", "sugar", "salt", "cheese", "onion", "pepper", "chicken", 
    "tomato", "garlic", "oil", "banana", "rice", "spinach", "carrot", "potato", "beef", "fish", 
    "lettuce", "bread", "corn", "pasta", "basil", "oregano", "chili", "honey", "yogurt", "cream", 
    "cucumber", "mushroom", "lemon", "vinegar", "ginger", "soy sauce", "tofu", "cabbage", "beans", "peas"
]

# Initialize the TTS engine
engine = pyttsx3.init()

# Set the voice (male/female)
voices = engine.getProperty('voices')
# Change to a different voice, e.g., 0 for male, 1 for female
engine.setProperty('voice', voices[1].id)  # Use voice index 0 for male or 1 for female

# Set the speed (rate) of speech
engine.setProperty('rate', 150)  # Default rate is 200; 150 is slower, and 250 is faster

# Function to speak a message
def speak_message(message):
    engine.say(message)
    engine.runAndWait()

# Function to extract ingredients from the user's input text
def extract_ingredients(user_input):
    doc = nlp(user_input)
    extracted_ingredients = set()
    for chunk in doc.noun_chunks:
        ingredient = chunk.text.lower()
        if ingredient in ingredient_list:
            extracted_ingredients.add(ingredient)
    return extracted_ingredients

# Capture user input using the microphone and process after silence
def listen_to_microphone():
    recognizer = sr.Recognizer()
    available_ingredients = set()
    silence_threshold = 5  # Time in seconds to wait for silence before processing
    last_speech_time = time.time()  # Track the last speech time

    with sr.Microphone() as source:
        speak_message("I am a food AI. Please tell me the ingredients you have...")

        recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for ambient noise
        
        # Start listening and handle pauses
        while True:
            try:
                time.sleep(3)
                print("Listening...")
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)  # Adjusted timeout
                user_input = recognizer.recognize_google(audio)
                print(f"User said: {user_input}")

                # Extract ingredients from the speech
                ingredients = extract_ingredients(user_input)
                if ingredients:
                    available_ingredients.update(ingredients)
                    print(f"Ingredients collected so far: {available_ingredients}")
                else:
                    print("No recognized ingredients found in your input.")

                # Update the last speech time
                last_speech_time = time.time()

            except sr.UnknownValueError:
                error_message = "Sorry, I couldn't understand what you said. Please try again."
                print(error_message)
                speak_message(error_message)

            except sr.RequestError as e:
                error_message = f"Could not request results from Google Speech Recognition service; {e}"
                print(error_message)
                speak_message(error_message)

            # Check for silence (no input for `silence_threshold` seconds)
            if time.time() - last_speech_time > silence_threshold:
                if available_ingredients:
                    response = f"You have the following ingredients: {', '.join(available_ingredients)}."
                    print(response)
                    speak_message(response)
                else:
                    response = "I couldn't catch any ingredients from your speech."
                    print(response)
                    speak_message(response)

                # Reset the ingredients and continue listening
                available_ingredients.clear()

# Start listening to the microphone
listen_to_microphone()
