from gtts import gTTS

class Text_to_Sound:

    def __init__(self):
        pass

    def to_sound(self,msg):
        tts = gTTS(text=msg, lang='zh')
        tts.save("/content/drive/MyDrive/ColabNotebooks/AI_sound_to_video/resources/response.wav")

if __name__ == "__main__":
  text_to_sound = Text_to_Sound()
  text_to_sound.to_sound("你好,我是AI")