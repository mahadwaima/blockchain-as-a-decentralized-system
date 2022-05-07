"""
Done by : Maha dwaima.
"""
import hashlib

class MahaCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Maha sends 5 GC to Amal"
t2 = "Amal sends 3.2 GC to Mohammed"
t3 = "Mohammed sends 4.2 GC to Ali"
t4 = "Ali sends 1.1 GC to Maha"

block1 = MahaCoinBlock('firstblock', [t1, t2])

print(f"Block 1 data: {block1.block_data}")
print(f"Block 1 hash: {block1.block_hash}")

block2 = MahaCoinBlock(block1.block_hash, [t3, t4])

print(f"Block 2 data: {block2.block_data}")
print(f"Block 2 hash: {block2.block_hash}")