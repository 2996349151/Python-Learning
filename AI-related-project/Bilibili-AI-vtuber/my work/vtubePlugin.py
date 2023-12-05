import asyncio
import pyvts


class VtuPlugin:
    def __init__(self):
        self.plugin_info = plugin_info = {
                                            "plugin_name": "AI vtuber",
                                            "developer": "DZJ",
                                            "authentication_token_path": "./token.txt"
}
        self.action_list = []

    async def actionInit(self):

        vts = pyvts.vts(plugin_info=self.plugin_info)
        try:
            await vts.connect()
        except ConnectionRefusedError:
            raise '请先打开VTS，并打开API开关！'
        print('请在live2D VTS弹窗中点击确认！')
        await vts.request_authenticate_token()  # get token
        await vts.write_token()
        await vts.request_authenticate()  # use token

        response_data = await vts.request(vts.vts_request.requestHotKeyList())
        hotkey_list = []
        for hotkey in response_data['data']['availableHotkeys']:
            hotkey_list.append(hotkey['name'])
        print('读取到所有模型动作:', hotkey_list)
        self.action_list = hotkey_list

        await vts.close()

    async def play_action(self,action_index):

        vts = pyvts.vts(plugin_info=self.plugin_info)
        await vts.connect()
        await vts.read_token()
        await vts.request_authenticate()  # use token

        if action_index > len(self.action_list) - 1:
            raise '动作不存在'
        send_hotkey_request = vts.vts_request.requestTriggerHotKey(self.action_list[action_index])
        await vts.request(send_hotkey_request)
        await vts.close()


vtu = VtuPlugin()

