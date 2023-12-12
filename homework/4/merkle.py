import hashlib

class MerkleNode(object):
    def __init__(self,left=None,right=None,data=None):
        self.left = left
        self.right = right
        # data中保存着哈希值
        self.data = data

def hash_node(addresss):
   # blocks = ['node1', 'node2', 'node3', 'node4', 'node5']  # 示例数据，包含4个节点
    nodes = []  # 节点初始化
    #print("节点哈希值：")
    for element in addresss:  # 遍历示例数据
        sha256 = hashlib.sha256(element.encode("utf-8")).hexdigest()  # 摘要算法
        nodes.append(MerkleNode(data=sha256))  # 添加至默克尔树节点中
        #print(element + ":", sha256)
    return nodes

def create_tree(nodes):
    list_len = len(nodes)
    #print("begin:", list_len)
    if list_len == 0:
        return 0
    else:
        while list_len %2 != 0:
            nodes.extend(nodes[-1:])
            list_len = len(nodes)
        secondary = []

        #两两合并节点，并计算其哈希值
        for k in [nodes[x:x+2] for x in range(0,list_len,2)]:
            d1 = k[0].data
            d2 = k[1].data
            # if d1 > d2:
            #     d1 = d1+d2
            # else:
            #     d1 = d2 + d1
            sha256 = hashlib.sha256((d1+d2).encode("utf-8"))
            new_data = sha256.hexdigest()
            node = MerkleNode(left=k[0],right=k[1],data=new_data)
            secondary.append(node)
        if len(secondary) == 1:
            return secondary[0]
        else:
            return create_tree(secondary)

#利用广度优先搜索算法对节点数据进行遍历
def dbf_proof(root, address):
    #print('开始广度优先搜索，构建默克尔树...')
    i=0
    queue = []
    queue2 = []
    queue.append(root)
    queue2.append(root.data)
    index = -1
    target = hashlib.sha256(address.encode("utf-8")).hexdigest()
    while(len(queue)>0):
        e = queue.pop(0)
        i+=1
        #print("Hash Value:"+str(i),e.data)
        if e.left != None:
            queue.append(e.left)
            queue2.append(e.left.data)
        if e.right != None:
            queue.append(e.right)
            queue2.append(e.right.data)
        if e.data == target:
            index = i - 1

    #print(len(queue2), queue2)
    #queue.append(root.data) # 先添加根
    if index < 0:
        return []
    while index > 0:
        if index % 2 == 0:
            queue.append(queue2[index-1])
        else:
            queue.append(queue2[index+1])
        parent = int((index - 1) / 2)
        index = parent
    return queue

# 获得证明
def get_proof(inputs, address):
    nodes = hash_node(inputs)
    root = create_tree(nodes)
    #print("root:", root.data)
    return dbf_proof(root, address)

# 验证证明
def verify_proof(root, inputs,  address):
    list = get_proof(inputs, address)
    print(list)
    if len(list) == 0:
        return False
    # cal_root = list[0]
    # if cal_root != root:
    #     return False
    target = hashlib.sha256(address.encode("utf-8")).hexdigest()
    dd = target
    for element in list:
        if dd > element:
            dd = dd + element
        else:
            dd = element + dd
        dd = hashlib.sha256(dd.encode("utf-8")).hexdigest()
    print("get root:", dd)
    if root == dd:
        return True
    else:
        return False

etheraddrs1 = ['0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db',
              '0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB',
              '0x617F2E2fD72FD9D5503197092aC168c91465E7f2',
              '0x17F6AD8Ef982297579C203069C1DbfFE4348c372']
white_addr1 = '0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB'
root1 = '2c0caea483bad825ff93a49c0a76162d9833668183b08c349553a1d2ba1eee17'


if __name__ == "__main__":
    resut = get_proof(etheraddrs1, white_addr1)
    print(resut)
    #print(verify_proof(root1, etheraddrs1, white_addr1))

