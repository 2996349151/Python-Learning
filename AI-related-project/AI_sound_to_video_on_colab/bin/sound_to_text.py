import whisper

class Sound_to_Text:
    def __init__(self):
        pass

    def to_text(self, filename):
        model = whisper.load_model("base")
        result = model.transcribe(filename,fp16=False)
        return result["text"]


if __name__ == "__main__":
    sound_to_text = Sound_to_Text()
    print(sound_to_text.to_text("/content/drive/MyDrive/ColabNotebooks/AI_sound_to_video/resources/test/test.mp3"))