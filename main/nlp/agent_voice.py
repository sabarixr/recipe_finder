import pyaudio
import os 
from faster_whisper import WhisperModel

num_cores = os.cpu_count()
whisper_size = "base"
whisper_model = WhisperModel(
    whisper_size, device = "cpu",
    compute_type = 'int8', 
    cpu_threads = num_cores//3, 
    num_workers = num_cores//3
    )

