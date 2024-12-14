import os
import re



from faster_whisper import WhisperModel
language = "en"  # Restrict transcription to English

# Initialize the Whisper model
num_cores = os.cpu_count()
whisper_size = "base"
whisper_model = WhisperModel(
    whisper_size,
    device="cpu",
    compute_type="auto",
    cpu_threads=num_cores // 2,
    num_workers=num_cores // 2,
)


def speech_to_text(audio_path):
    """Transcribes audio to text using Whisper."""
    print("Transcribing audio...")
    segments, _ = whisper_model.transcribe(audio_path, language=language)
    return ''.join(segment.text for segment in segments)

def extract_prompt(transcribe, wake_word):
    """Extract the prompt following the wake word."""
    print("Extracting prompt...")
    print(transcribe)
    pattern = rf"\b{re.escape(wake_word)}[\s,.?!]*([A-Za-z0-9].*)"
    match = re.search(pattern, transcribe, re.IGNORECASE)
    return match.group(1).strip() if match else None
