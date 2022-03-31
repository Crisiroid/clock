from hashlib import sha256

def u_hash(*args):
    h_text = ""; g_hash = sha256()
    for arg in args:
        h_text += str(arg)

    g_hash.update(h_text.encode('utf-8'))
    return g_hash.hexdigest()

class Block():
    m_data = None
    c_hash = None
    a_nonce = 0
    p_hash = "0" * 64

    def __init__(self, m_data, block_n = 0):
        self.m_data = m_data
        self.block_n = block_n


    def hash(self):
        return u_hash(self.p_hash, self.block_n, self.m_data, self.a_nonce)
class BlockChain():
    pass





def main():
    block = Block("Hello", 1)


if __name__ == '__main__':
    main()