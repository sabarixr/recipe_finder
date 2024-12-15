import os
import tkinter as tk
from tkinter import ttk
from nlp.speak_message import generate_audio
from nlp.agent_voice import extract_prompt, speech_to_text
import markdown2
import threading
import speech_recognition as sr
import os
from PIL import Image, ImageTk


import tempfile
from decision_maker import get_response
from init import create_recipe_graph

wake_word = "hey"

r = sr.Recognizer()

def on_scroll(event):
    """Handle two-finger scrolling event."""
    chat_canvas.yview_scroll(int(event.delta / 120), "units")

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
    chat_canvas.yview_moveto(1.0)

# Usage example:
def send_message(promt = None, is_voice = None):
    if promt is None:
        user_message = entry_box.get()
    else:
        user_message = promt
    if user_message.strip():
        add_message("User", user_message, align="right")
        entry_box.delete(0, tk.END)
        response = get_response(G, user_message, options_var.get(), time_entry.get(), cuisines_var.get(),  fastest_var.get())
        
        if response:
            add_message("Agent", response, align="left")
            
        else:
            add_message("Agent", "Sorry, I couldn't process your request.", align="left")
        
        if is_voice:
            generate_audio(response)
    else:
        add_message("Agent", "Please provide the available ingreadints", align="left")

# Main Window
root = tk.Tk()
root.geometry("1000x700")
root.title("Let AI Cook")
root.config(bg="#272425")

# Configure Grid
root.columnconfigure(0, weight=99)  # Main content (chat area)
root.columnconfigure(1, weight=1)   # Sidebar
root.rowconfigure(0, weight=0)      # Header (fixed height)
root.rowconfigure(1, weight=1)      # Chat area (resizable)
root.rowconfigure(2, weight=0)      # Footer (fixed height)


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
header_frame.grid(row=0, column=0, sticky="nsew", padx=(50, 0))  
header_frame.grid_columnconfigure(0, weight=1)

header_label = tk.Label(header_frame, text="Let AI Cook", bg="#272425", fg="white", font=("Arial", 24, "bold"))
header_label.pack(anchor="center", pady=10)

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

# Bind two-finger scroll
chat_canvas.bind("<MouseWheel>", on_scroll)
chat_canvas.bind("<Button-4>", on_scroll)  # Scroll up
chat_canvas.bind("<Button-5>", on_scroll) 

sidebar_frame = tk.Frame(root, bg="#1e1e1e", width=250)
sidebar_frame.grid(row=0, column=1, rowspan=3, sticky="nsew")  # Spanning all rows (header, chat, footer)
sidebar_frame.grid_rowconfigure(0, weight=1)

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

options_var = tk.StringVar(value="")  # Variable to store the selected option
options_section = add_section(sidebar_frame, "Dietary Options", options_var)  # Add the options section
options_frame = tk.Frame(options_section, bg="#323235")
options_frame.pack()

# Updated list of options
options = [
    "plant-based", "gluten-free", "high-protein", 
    "comfort-food", "vegetarian", "low-carb", "sugar-free"
]

# Render buttons in a 3-per-row layout
for i, option in enumerate(options):
    row = i // 3  # Calculate the row index
    col = i % 3   # Calculate the column index
    tk.Radiobutton(
        options_frame, 
        text=option, 
        variable=options_var, 
        value=option, 
        bg="#323235", 
        fg="white", 
        font=("Arial", 12), 
        selectcolor="#4A4A4A"
    ).grid(row=row, column=col, padx=10, pady=5, sticky="w")

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

cuisines_var = tk.StringVar(value="")  # Variable to store selected cuisine
cuisines_section = add_section(sidebar_frame, "Cuisines", cuisines_var)  # Add the cuisines section
cuisines_frame = tk.Frame(cuisines_section, bg="#323235")
cuisines_frame.pack()

# List of cuisines
cuisines = [
    "Indian", "Arabian", "Chinese", "Spanish", "Italian", "Middle Eastern", 
    "Japanese", "Asian", "Mediterranean", "Mexican", "American", "French", 
    "Thai", "Vietnamese", "British", "German", "Malaysian"
]

# Render buttons in 3-per-row layout
for i, cuisine in enumerate(cuisines):
    row = i // 3  # Calculate the row index
    col = i % 3   # Calculate the column index
    tk.Radiobutton(
        cuisines_frame, 
        text=cuisine, 
        variable=cuisines_var, 
        value=cuisine, 
        bg="#323235", 
        fg="white", 
        font=("Arial", 12), 
        selectcolor="#4A4A4A"
    ).grid(row=row, column=col, padx=10, pady=5, sticky="w")
# Footer
footer_frame = tk.Frame(root, bg="#272425", height=80)
footer_frame.grid(row=2, column=0, sticky="nsew", padx=(50, 0))  # Matches chat area width

footer_frame.grid_columnconfigure(0, weight=1)  # Spacer before entry box
footer_frame.grid_columnconfigure(1, weight=8)  # Entry box width proportional to chat area
footer_frame.grid_columnconfigure(2, weight=0)  # Button column
footer_frame.grid_columnconfigure(3, weight=1)  # Spacer after button (remaining space)

entry_box = tk.Entry(
    footer_frame,
    bg="#323235",
    fg="white",
    font=("Arial", 14),
    insertbackground="white",
    bd=0,
    relief=tk.FLAT,
    width=80,
    highlightthickness=9,
    highlightbackground="#323235",
    highlightcolor="#323235"
)
entry_box.grid(row=0, column=1, padx=(10, 5), pady=20, ipadx=10, ipady=10)

def create_rounded_button(canvas, x, y, size, image_path, command):
    img = Image.open(image_path)
    max_image_size = int(size * 0.7)  # Make the image 70% of the button size
    img.thumbnail((max_image_size, max_image_size), Image.Resampling.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    canvas.image = img_tk

    # Create an oval as the button background
    button_id = canvas.create_oval(x, y, x + size, y + size, fill="#323235", outline="#323235")

    # Calculate the center of the oval
    center_x = x + size // 2
    center_y = y + size // 2

    # Place the image at the center of the oval
    img_id = canvas.create_image(center_x, center_y, image=img_tk, anchor="center")

    # Bind click events to the command
    canvas.tag_bind(button_id, "<Button-1>", lambda e: command())
    canvas.tag_bind(img_id, "<Button-1>", lambda e: command())

    return img_id

def adjust_button_to_entry_height():
    entry_box_height = entry_box.winfo_height()

    send_button_canvas.config(width=entry_box_height, height=entry_box_height)
    create_rounded_button(send_button_canvas, 0, 0, entry_box_height, image_path, send_message)

image_path = os.path.join(os.path.dirname(__file__), 'assets', 'send-message.png')
send_button_canvas = tk.Canvas(footer_frame, bg="#272425", highlightthickness=0)
send_button_canvas.grid(row=0, column=2, padx=(5, 10), pady=20)  # Reduced padding between entry and button

footer_frame.after(10, adjust_button_to_entry_height)

entry_box.bind("<Return>", lambda event: send_message())


# def run_speech_agent():
#     threading.Thread(target=start_listening, daemon=True).start()

# run_speech_agent()

root.mainloop()
