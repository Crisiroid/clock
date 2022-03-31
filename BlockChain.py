from hashlib import sha256
class Block():
    m_data = None
    c_hash = None
    a_nonce = 0
    p_hash = "0" * 64

    def __init__(self, m_data, block_n = 0):
        self.m_data = m_data
        self.block_n = block_n
class BlockChain():
    pass





def main():
    block = Block("Hello", 1)


if __name__ == '__main__':
    main()