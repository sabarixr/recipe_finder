import speech_recognition as sr
from nlp_part import extract_ingredients  


def process_wav_file(file_path):
    recognizer = sr.Recognizer()
    available_ingredients = set()

    with sr.AudioFile(file_path) as source:
        print(f"Processing {file_path}...")
        audio = recognizer.record(source)  
        try:
            user_input = recognizer.recognize_google(audio)
            print(f"Recognized speech: {user_input}")

            # Extract ingredients from the speech
            ingredients = extract_ingredients(user_input)
            if ingredients:
                available_ingredients.update(ingredients)
                print(f"Ingredients found: {available_ingredients}")
            else:
                print("No recognized ingredients found in the audio.")
        except sr.UnknownValueError:
            error_message = "Sorry, I couldn't understand the audio. Please try again."
            print(error_message)

        except sr.RequestError as e:
            error_message = f"Could not request results from Google Speech Recognition service; {e}"
            print(error_message)

    if available_ingredients:
        response = f"You have the following ingredients: {', '.join(available_ingredients)}."
        print(response)
    else:
        response = "I couldn't find any ingredients in the audio."
        print(response)

file_path = "path_to_your_file.wav"
process_wav_file(file_path)
