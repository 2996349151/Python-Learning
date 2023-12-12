from transformers import AutoTokenizer, AutoModel
import torch

class AI:
    def __init__(self):
        torch.cuda.is_available()
        self.tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True)
        self.model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True).half().cuda()
        self.model = self.model.eval()

    def chat(self,msg):
        self.response, _ = self.model.chat(self.tokenizer, msg, history=[])
        return self.response