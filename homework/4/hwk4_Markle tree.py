# -*- coding: UTF-8 -*-

"""
 * 请勿改变本代码文件名，类名，方法名，方法参数类型，方法返回值类型
"""

"""
	/**
	 * 生成给定账户的默克尔树证明，本方法按照竞赛题目要求完成
	 * 
	 * @param whiteList
	 *            账户白名单
	 * @param account
	 *            给定的账户
	 * 
	 * @return 给定账户的默克尔树证明, 如果账户不在白名单内，返回空的字符串数组new String[0];
	 */
"""
import hashlib
import math
from web3 import Web3

class Tree():
    def __init__(self, root=None, left=None, right=None, value=None):
        self.value = value
        self.root = root
        self.left = left
        self.right = right
        if self.left != None:
            self.left.root = self
        if self.right != None:
            self.right.root = self

    # deep copy a tree
    def deep_copy(self, root=None):
        T = Tree()
        T.value = self.value
        T.root = root
        T.hash_value = self.hash_value
        if self.left != None:
            T.left = self.left.deep_copy(root=T)
        if self.right != None:
            T.right = self.right.deep_copy(root=T)
        return T

    # return the hash value of a tree
    def hash_value(self):
        if self.left == None and self.right == None:
            return self.hashKeccak([self.value],['address'])
        else:
            l = self.left.hash_value()
            r = self.right.hash_value()

            if l >= r:
                return self.hashKeccak([l,r],['bytes32','bytes32'])
            else:
                return self.hashKeccak([r,l],['bytes32','bytes32'])

    # search a value in a tree and return the
    def search(self, v):
        if v == self.value:
            return list()
        elif v in self.left.value:
            y = self.left.search(v)
            y.append(self.right.hash_value())
            return y
        elif v in self.right.value:
            y = self.right.search(v)
            y.append(self.left.hash_value())
            return y

    # print the value of a tree from root to leaf
    def show(self):
        if self.left == None and self.right == None:
            print(self.value)
        else:
            self.left.show()
            self.right.show()

    def hashKeccak(self, _message, _type):
        w3 = Web3()
        return w3.to_hex(w3.solidity_keccak(abi_types=_type,values=_message))

class MerkleTree(object):
    #creat a merkle tree
    def makeTree(self, whiteList):
        whiteList = [Tree(value=i) for i in whiteList]
        if int(math.pow(2, math.ceil(math.log(len(whiteList), 2))) - len(whiteList)) != 0:
            whiteList.extend(
                [None for i in range(int(math.pow(2, math.ceil(math.log(len(whiteList), 2))) - len(whiteList)))])
        while len(whiteList) != 1:
            newList = []
            for i in range(int(len(whiteList) / 2)):
                if whiteList[2 * i] != None:
                    if whiteList[2 * i + 1] != None:
                        t = Tree(value=whiteList[2 * i].value + whiteList[2 * i + 1].value, left=whiteList[2 * i].deep_copy(),
                                 right=whiteList[2 * i + 1].deep_copy())
                    else:
                        t = Tree(value=whiteList[2 * i].value + whiteList[2 * i].value, left=whiteList[2 * i].deep_copy(),
                                 right=whiteList[2 * i].deep_copy())
                else:
                    t = None
                newList.append(t)
            whiteList = newList
        print(whiteList[0].hash_value())
        print('-----')
        return whiteList[0]

    # return the merkle proof
    def merkleProof(self, whiteList, account):
        t = self.makeTree(whiteList)
        if account not in t.value:
            return [""]
        else:
            answer = t.search(account)
            return answer

solution = MerkleTree()
whiteLists = ['0x5B38Da6a701c568545dCfcB03FcB875f56beddC4', '0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2', '0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db', '0x78731D3Ca6b7E34aC0F824c42a7cC18A495cabaB', '0x617F2E2fD72FD9D5503197092aC168c91465E7f2', '0x17F6AD8Ef982297579C203069C1DbfFE4348c372', '0x5c6B0f7Bf3E7ce046039Bd8FABdfD3f9F5021678', '0x03C6FcED478cBbC9a4FAB34eF9f40767739D1Ff7', '0x1aE0EA34a72D944a8C7603FfB3eC30a6669E454C', '0x0A098Eda01Ce92ff4A4CCb7A4fFFb5A43EBC70DC', '0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c', '0x95291f083b42901A91D6EFA0Dfe4c7dcAdBFD293', '0x30044b7C080A6e456386d5b9c370Dc7c259AE2cd', '0x3051a91aeEDB09bA09a67323Bd0C9fB6061FbF86', '0x4f1135c0Dd6D53EB3B1E32d4F256F30d035f13E3', '0xc2329F565d418Bc74A0cD17E8464D5E4ba7f8B02', '0x6dBe810e3314546009bD6e1B29f9031211CdA5d2', '0x14723A09ACff6D2A60DcdF7aA4AFf308FDDC160C', '0x4B0897b0513fdC7C541B6d9D7E929C4e5364D2dB', '0x583031D1113aD414F02576BD6afaBfb302140225', '0xdD870fA1b7C4700F2BD7f44238821C26f7392148']


target = '0x14723A09ACff6D2A60DcdF7aA4AFf308FDDC160C'
result = solution.merkleProof(whiteLists, target)

for i in result:
    print(i)
