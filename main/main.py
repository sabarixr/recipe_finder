import os
import tkinter as tk
from tkinter import ttk
from nlp.speak_message import generate_audio
from nlp.agent_voice import extract_prompt, speech_to_text
import markdown2
import threading
import speech_recognition as sr
import os

import tempfile
from decision_maker import get_response
from init import create_recipe_graph

wake_word = "hey"

r = sr.Recognizer()


def process_audio(audio_data):
    """Processes audio data to recognize speech and extract the prompt."""
    try:
        # Save the raw audio data to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio_file:
            temp_audio_file.write(audio_data.get_wav_data())
            temp_audio_path = temp_audio_file.name
        
        # Transcribe the temporary audio file
        transcribe = speech_to_text(temp_audio_path)
        cleaned_prompt = extract_prompt(transcribe, wake_word)

        if cleaned_prompt:
            set_text(cleaned_prompt)  # Sends recognized text to the UI
    except Exception as e:
        print(f"Error processing audio: {e}")
    finally:
        # Clean up temporary audio file
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)

def start_listening():
    """Continuously listens to the microphone and transcribes speech."""
    print("Agent is listening...")

    with sr.Microphone() as source:
        # Adjust for ambient noise
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=2)

        while True:
            try:
                print("Listening for speech...")
                audio_data = r.listen(source, timeout=None, phrase_time_limit=10)
                # Process audio in a separate thread
                thread = threading.Thread(target=process_audio, args=(audio_data,))
                thread.start()
                thread.join() 
            except sr.WaitTimeoutError:
                print("Listening timed out, restarting...")
            except Exception as e:
                print(f"Error during listening: {e}")




G = create_recipe_graph()
message_count = 0 

def set_text(prompt):
    send_message(promt=prompt,is_voice=True)


def add_message(sender, message, align="left"):
    global message_count

    # Message Frame
    message_frame = tk.Frame(chat_area, bg="#272425", pady=10, padx=10)
    message_frame.grid(row=message_count, column=0, sticky="ew", padx=10, pady=5)
    message_frame.grid_columnconfigure(0, weight=1)

    # Adjust the Canvas for a proper oval
    icon = tk.Canvas(message_frame, width=50, height=50, bg="#272425", highlightthickness=0)
    icon.create_oval(5, 10, 45, 40, fill="#323235", outline="#323235")

    # Display sender and message with increased font size
    text_font = ("Arial", 14)  # Adjust font size

    # If the message is from "Agent" and has Markdown, parse it
    if sender == "Agent":
        message_label = tk.Label(message_frame, text=message, font=text_font, wraplength=700, bg="#272425", fg="#FFFFFF", justify=align)
    else:
        message_label = tk.Label(message_frame, text=message, font=text_font, wraplength=700, bg="#272425", fg="#FFFFFF", justify=align)

    # Pack elements based on alignment
    if align == "right":
        icon.grid(row=0, column=1, padx=(10, 0), sticky="e")
        message_label.grid(row=1, column=0, columnspan=2, sticky="e")
    else:  # Align to the left
        icon.grid(row=0, column=0, padx=(0, 10), sticky="w")
        message_label.grid(row=1, column=0, columnspan=2, sticky="w")

    # Increment message count for the next message
    message_count += 1

# Usage example:
def send_message(promt = None, is_voice = None):
    if promt is None:
        user_message = entry_box.get()
    else:
        user_message = promt
    if user_message.strip():
        add_message("User", user_message, align="right")
        entry_box.delete(0, tk.END)
        response = get_response(G, user_message, var_options.get(), time_entry.get(), cuisines_var.get(),  fastest_var.get())
        
        if response:
            add_message("Agent", response, align="left")
        else:
            add_message("Agent", "Sorry, I couldn't process your request.", align="left")
        generate_audio(response)

# Main Window
root = tk.Tk()
root.geometry("1000x700")
root.title("Let AI Cook")
root.config(bg="#272425")

# Configure Grid
root.columnconfigure(0, weight=99)  # Main content (70% width)
root.columnconfigure(1, weight=1)  # Sidebar (30% width)
root.rowconfigure(1, weight=1)     # Chat area (main section)

# Style Scrollbar
style = ttk.Style(root)
style.theme_use("clam")

style.configure("Vertical.TScrollbar",
                gripcount=0,
                background="#323235",
                darkcolor="#3C3C3C",
                lightcolor="#4A4A4A",
                troughcolor="#1E1E1E",
                bordercolor="#272425",
                arrowcolor="#FFFFFF")
style.map("Vertical.TScrollbar",
          background=[["active", "#4C4C4C"], ["pressed", "#5A5A5A"]])

# Header
header_frame = tk.Frame(root, bg="#272425", height=60)
header_label = tk.Label(header_frame, text="Let AI Cook", bg="#272425", fg="white", font=("Arial", 24, "bold"))
header_label.pack(anchor="center", pady=10)
header_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=(50, 50))

# Chat Area
chat_frame = tk.Frame(root, bg="#272425")
chat_frame.grid(row=1, column=0, sticky="nsew", padx=(50, 0), pady=(10, 10))
chat_frame.grid_columnconfigure(0, weight=1)
chat_frame.grid_rowconfigure(0, weight=1)

chat_canvas = tk.Canvas(chat_frame, bg="#272425", highlightthickness=0, bd=0)
chat_canvas.grid(row=0, column=0, sticky="nsew")

chat_scrollbar = ttk.Scrollbar(chat_frame, orient="vertical", style="Vertical.TScrollbar", command=chat_canvas.yview)
chat_scrollbar.grid(row=0, column=1, sticky="ns")

chat_area = tk.Frame(chat_canvas, bg="#272425")
chat_area.grid_columnconfigure(0, weight=1)
chat_window = chat_canvas.create_window((0, 0), window=chat_area, anchor="nw")

# Bind canvas width changes to adjust the width of chat_area
def resize_chat_area(event):
    chat_canvas.itemconfig(chat_window, width=event.width)

chat_canvas.bind("<Configure>", resize_chat_area)
chat_area.bind("<Configure>", lambda e: chat_canvas.configure(scrollregion=chat_canvas.bbox("all")))

# Sidebar
sidebar_frame = tk.Frame(root, bg="#1e1e1e", width=250)
sidebar_frame.grid(row=1, column=1, sticky="nsew")

# Helper for adding sections
def add_section(parent, title, var):
    section_frame = tk.Frame(parent, bg="#323235", pady=10, padx=10)
    section_label = tk.Label(section_frame, text=title, bg="#323235", fg="white", font=("Arial", 14, "bold"))
    section_label.pack(anchor="w")
    
    clear_button = tk.Button(section_frame, text="Clear", bg="#4A4A4A", fg="white", font=("Arial", 12), command=lambda: clear_selection(var))
    clear_button.pack(side="bottom", pady=(5, 10))

    tk.Canvas(section_frame, height=2, bg="#4A4A4A", highlightthickness=0).pack(fill="x", pady=(5, 10))
    section_frame.pack(fill=tk.X, pady=5, padx=10)
    return section_frame

def clear_selection(var):
    var.set("")  

var_options = tk.StringVar(value="")
options_section = add_section(sidebar_frame, "Options", var_options)
options_grid = tk.Frame(options_section, bg="#323235")
options_grid.pack()

options = ["Sugar Free", "Gluten Free", "Low Carb", "Plant Based"]
for i, option in enumerate(options):
    tk.Radiobutton(options_grid, text=option, variable=var_options, value=option, bg="#323235", fg="white", font=("Arial", 12), selectcolor="#4A4A4A").grid(row=i//2, column=i%2, padx=5, pady=5, sticky="w")

# Time Constraint Section
time_var = tk.StringVar(value="")
time_section = add_section(sidebar_frame, "Time Constraint", time_var)
time_frame = tk.Frame(time_section, bg="#323235")
time_frame.pack(fill=tk.X, pady=(10, 5))

time_label = tk.Label(time_frame, text="Minutes:", bg="#323235", fg="white", font=("Arial", 12))
time_label.pack(side="left", padx=(5, 5))

time_entry = tk.Entry(time_frame, bg="#4A4A4A", fg="white", font=("Arial", 12), bd=0, insertbackground="white")
time_entry.pack(side="left", padx=(5, 5), pady=5)

fastest_var = tk.BooleanVar(value=False)  # Default is unchecked
fastest_check = tk.Checkbutton(
    time_section, 
    text="Fastest", 
    variable=fastest_var,  # Bind the BooleanVar
    bg="#323235", 
    fg="white", 
    font=("Arial", 12), 
    selectcolor="#4A4A4A"
)
fastest_check.pack(anchor="w", padx=5, pady=5)

cuisines_var = tk.StringVar(value="")
cuisines_section = add_section(sidebar_frame, "Cuisines", cuisines_var)
cuisines_frame = tk.Frame(cuisines_section, bg="#323235")
cuisines_frame.pack()

cuisines = ["Indian", "Arabian", "Chinese"]
for i, cuisine in enumerate(cuisines):
    tk.Radiobutton(cuisines_frame, text=cuisine, variable=cuisines_var, value=cuisine, bg="#323235", fg="white", font=("Arial", 12), selectcolor="#4A4A4A").grid(row=0, column=i, padx=10, pady=5, sticky="w")

# Footer
footer_frame = tk.Frame(root, bg="#272425", height=80)
footer_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=(50, 50))

footer_frame.grid_columnconfigure(0, weight=1)  # Left spacer
footer_frame.grid_columnconfigure(1, weight=0)  # Entry box
footer_frame.grid_columnconfigure(2, weight=0)  # Button
footer_frame.grid_columnconfigure(3, weight=1)  # Right spacer

entry_box = tk.Entry(
    footer_frame,
    bg="#323235",
    fg="white",
    font=("Arial", 14),
    insertbackground="white",
    bd=0,
    relief=tk.FLAT,
    width=80,
    highlightthickness=9,  # Adds padding by increasing the highlight area
    highlightbackground="#323235",  # Matches the background to make it invisible
    highlightcolor="#323235"  # Matches background for focus appearance
)
entry_box.grid(row=0, column=1, padx=(10, 5), pady=20, ipadx=10, ipady=10)

def create_rounded_button(canvas, x, y, size, image_path, command):
    # Load the image
    img = tk.PhotoImage(file=image_path)
    canvas.image = img  # Store the reference to prevent garbage collection

    # Create an oval as the button background
    button_id = canvas.create_oval(x, y, x + size, y + size, fill="#323235", outline="#323235")

    # Place the image inside the button
    img_id = canvas.create_image(x + size // 6, y + size // 6, image=img, anchor=tk.CENTER)

    # Bind click events to the command
    canvas.tag_bind(button_id, "<Button-1>", lambda e: command())
    canvas.tag_bind(img_id, "<Button-1>", lambda e: command())

    return img_id  # Return the image ID for future reference

image_path = "/home/eclipwze/AMRITA-S3/AI/project/main/assets/send-message.png"

# Usage in the main code
image_path = os.path.join(os.path.dirname(__file__), 'assets', 'send-message.png')
send_button_canvas = tk.Canvas(footer_frame, width=50, height=50, bg="#272425", highlightthickness=0)
create_rounded_button(send_button_canvas, 5, 5, 40, image_path, send_message)
send_button_canvas.grid(row=0, column=2, padx=10, pady=20)

# Bind Enter key to send message
entry_box.bind("<Return>", lambda event: send_message())
def run_speech_agent():
    threading.Thread(target=start_listening, daemon=True).start()

# Start speech recognition
run_speech_agent()

root.mainloop()
