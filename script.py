from blockchain import Blockchain

# Inititiates values for blockchain
block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

# Creates new blockchain and prints the empty data
local_blockchain = Blockchain()
local_blockchain.print_blocks()

# Adds transactions into the blockchain
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)

# Prints the blocks to verify they were added
local_blockchain.print_blocks()

# Changes one of the previous blocks and verifies if the chain has changed
local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.validate_chain()