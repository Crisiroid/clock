from hashlib import sha256

def u_hash(*args):
    #hash generator
    h_text = ""; g_hash = sha256()
    for arg in args:
        h_text += str(arg)

    g_hash.update(h_text.encode('utf-8'))
    return g_hash.hexdigest()

class Block():
    #Main block
    m_data = None
    c_hash = None
    a_nonce = 0
    p_hash = "0" * 64

    def __init__(self, m_data, block_n = 0):
        self.m_data = m_data
        self.block_n = block_n


    def hash(self):
        return u_hash(self.p_hash, self.block_n, self.m_data, self.a_nonce)

    def __str__(self):
        return str("Block num: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n" %(self.block_n, self.hash(), self.p_hash, self.m_data, self.a_nonce))
class BlockChain():
    #creating block chain network
    hardiness = 4
    def __init__(self, chain = []):
        self.chain = chain

    def put_a(self, Block):
        self.chain.append({'hash': Block.hash(), 'Previous': Block.p_hash, 'Number': Block.block_n, 'Data': Block.m_data, 'nonce': Block.a_nonce})





def main():
    block = Block("Hello", 1)
    print(block)


if __name__ == '__main__':
    main()