import blivedm
import blivedm.models.web as web_models
import asyncio
import random
import vtubePlugin

import zhipuAI


class Blive():
    # Check url to see stream room ID

    def __init__(self,session):
        self.LIVE_ROOM_IDS = [
            30932709,
        ]
        self.session = session
        self.ai = zhipuAI.zhipuAI()

    async def run_client(self):
        room_id = random.choice(self.LIVE_ROOM_IDS)
        client = blivedm.BLiveClient(room_id, session=self.session)
        handler = MyHandler()
        client.set_handler(handler)
        client.start()

        try:
            await handler.vts.actionInit()
            i = 0
            while i<10000000000:
                await asyncio.sleep(1)
                i += 1
                if handler.play == 1:
                    await handler.vts.play_action(handler.emotion)
                    handler.play = 0
            client.stop()

            await client.join()
        finally:
            await client.stop_and_close()



class MyHandler(blivedm.BaseHandler):

    def __init__(self):
        self.ai = zhipuAI.zhipuAI()
        self.vts = vtubePlugin.VtuPlugin()
        self.response = ""
        self.emotion = 0
        self.play = 1


    def _on_danmaku(self, client: blivedm.BLiveClient, message: web_models.DanmakuMessage):
        print(f'[{client.room_id}] {message.uname}：{message.msg}')
        self.response = self.ai.invoke(message.uname,message.msg)
        self.emotion = int(self.ai.invoke(message.uname,"请根据下面的句子的情感只回答对应一个的数字0或1或2: " + self.response + "(0代表积极，1代表中立，2代表消极)"))
        self.play = 1
