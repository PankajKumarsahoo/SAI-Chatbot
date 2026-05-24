from gtts import gTTS
import uuid
import os

def text_to_audio(text):

    if not os.path.exists("audio"):
        os.makedirs("audio")

    filename = f"audio/{uuid.uuid4()}.mp3"

    tts = gTTS(
        text=text,
        lang="en"
    )

    tts.save(filename)

    return filename