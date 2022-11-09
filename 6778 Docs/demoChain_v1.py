"""
Description: Build a simple blockchain for demonstration in the Foundations of FinTech class.
                -Does not include proof-of-work and consensus algorithm
                -Based codes and articles of Gerald Nash (https://gist.github.com/aunyks) 
Author: Eshwar Venugopal
"""

import hashlib as hasher
import datetime as date

# Define what a demoChain block is
class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.hash_block()
  
  def hash_block(self):
    #sha = hasher.sha256()
    #sha.update(str(self.index).encode() + str(self.timestamp).encode() + str(self.data).encode() + str(self.previous_hash).encode())
    #return sha.hexdigest()
    header=(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode()
    inner_hash=hasher.sha256(header).hexdigest().encode()
    outer_hash=hasher.sha256(inner_hash).hexdigest()
    return outer_hash

# Generate genesis block
def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return Block(0, date.datetime.now(), "Genesis Block", "0")

# Generate all later blocks in the blockchain
def next_block(last_block):
  this_index = last_block.index + 1
  this_timestamp = date.datetime.now()
  this_data = input("Hey! Input your data for block #{}: ".format(this_index)) + str(this_index)
  this_hash = last_block.hash
  return Block(this_index, this_timestamp, this_data, this_hash)

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 5

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!
  print ("Block #{} has been added to the blockchain!".format(block_to_add.index))
  print ("Hash: {}\n".format(block_to_add.hash)) 
  
 
# Print Blockchain contents
for i in range(0, num_of_blocks_to_add):
  print ("Block #", i, "of the blockchain contains:")
  print ("---Data #", blockchain[i].data) 
  print ("---Previous block hash #", blockchain[i].previous_hash) 
  print ("---This block hash #", blockchain[i].hash)
  print ("---Timestamp #", blockchain[i].timestamp) 