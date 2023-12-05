import zhipuai
#from gtts import gTTS

class zhipuAI():
    def __init__(self):
        zhipuai.api_key = "03a209380b8ddcaee4e88b70e036e013.aS4Ct4yyUNA8lXRs"

    def invoke(self,name,msg):
        response = zhipuai.model_api.invoke(
            model="chatglm_turbo",
            prompt=[{"role": name, "content": msg}]
        )
        Response = response['data']['choices'][0]['content'].replace("\"","").strip()
        print("AI response:",Response)
        return Response
        #tts = gTTS(text=Response, lang='zh-CN')
        #tts.save("response.mp3")