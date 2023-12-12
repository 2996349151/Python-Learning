import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
        self.target_hash = '0x23456789'

    def calculate_hash(self):
        hash_string = str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(hash_string.encode()).hexdigest()

    # 1 工作量证明
    def mine_block(self, difficulty):
        # add your code here...
        requirement = '0' * difficulty
        start = datetime.datetime.now()
        while self.hash.startswith(requirement) == False:
            self.nonce += 1
            self.hash = self.calculate_hash()
        end = datetime.datetime.now()
        print(str(self.data) + 'Mining success!')
        print('Mining time:', end - start)


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 6
    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    # 2
    def add_block(self, data):
        # add your code here
        prev_hash = self.chain[-1].hash
        b = Block(data,prev_hash)
        b.mine_block(self.difficulty)
        self.chain.append(b)

    def print_chain(self):
        for block in self.chain:
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)
            print("Nonce:", block.nonce)
            print("-----------------------")

# 创建一个区块链实例
my_blockchain = Blockchain()

# 添加一些示例数据块
my_blockchain.add_block("Block 1 Data")
my_blockchain.add_block("Block 2 Data")
my_blockchain.add_block("Block 3 Data")

# 打印整个区块链
my_blockchain.print_chain()