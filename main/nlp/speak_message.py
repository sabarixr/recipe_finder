import time
from elevenlabs.client import ElevenLabs
from elevenlabs import Voice, VoiceSettings,save
from Secrets.load_env import ELEVEN_LABS_API, VOICE_ID
from api_fetch.gemeni import send_message


def generate_audio(food_item):
    start = time.time()
    client = ElevenLabs(
    api_key=ELEVEN_LABS_API,
    )

    audio = client.generate(
    text=send_message(food_item),
    voice=Voice(
            voice_id=VOICE_ID,
            settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
        ),
    model="eleven_turbo_v2_5"  #"eleven_multilingual_v2"
    )
    end =  time.time()
    save(audio, 'test.wav')
    print(end-start)