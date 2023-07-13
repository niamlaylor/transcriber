import os
from flask import Flask
import pvleopard

app = Flask(__name__)

ACCESS_KEY = os.getenv("ACCESS_KEY")
AUDIO_PATH = "./audio/audio1.mp3"

@app.route("/")
def home():
    leopard = pvleopard.create(access_key=ACCESS_KEY)

    transcript, words = leopard.process_file(AUDIO_PATH)
    print(transcript)
    return transcript