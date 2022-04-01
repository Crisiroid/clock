from encodings import utf_8
from hashlib import sha256

def generate_hash(*args):
    hash_text = ""
    generated_hash = sha256()
    for arg in args:
        hash_text += str(arg)
    generated_hash.update(hash_text.encode('utf_8'))
    return generated_hash.hexdigest()

class Block: 
    block_data = None
    current_hash = None
    nonce = 0
    previous_hash = "0"*64

    def __init__(self, block_data, block_number = 0):
        self.block_data = block_data
        self.block_number = block_number

    def hash(self):
        return generate_hash(self.previous_hash, self.block_number, self.block_data, self.nonce)
    def __str__(self):
        return str("Current Block Number: %s\nPrevious Block hash: %s\nCurrent Hash number: %s\nCurrent Data: %s\nNonce: %s\n" %(self.block_number, self.previous_hash, self.hash(), self.block_data, self.nonce))
class BlockChain: 
    dif = 4
    def __init__(self, chain = []):
        self.chain = chain
    def add_block_to_chain(self, block):
        self.chain.append({'hash': block.hash(), 'previous': block.previous_hash, 'number': block.block_number, 'data': block.block_data, 'nonce': block.nonce})
    def mine(self, block):
        try: 
            block.previous_hash = self.chain[-1].get('hash')
        except IndexError: 
            pass
        while True: 
            if block.hash()[:self.dif] == "0"*self.dif:
                self.add_block_to_chain(block)
                break
            else: 
                block.nonce += 1

def main():
    database = ["hello world", "This", "is Code", "With", "C"]
    block_chain = BlockChain()
    n = 0
    for x in database:
        n += 1
        block_chain.mine(Block(x, n))
    for b in block_chain.chain:
        print(b)

if __name__ == '__main__':
    main()
