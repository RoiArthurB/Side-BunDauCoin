#!/bin/python3

#
#	This is the blockchain structure for the fun crypto BunDauCoin
####
#	It's hightly inspired by this article:
#	 https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b 
#

from datetime import datetime
import hashlib as hasher

# Defining the structure of a BunDauBlock
class BDBlock:
	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block()

	def __str__(self):
		return 'BunDauBlock #{}'.format(self.index)

	def hash_block(self):
		# Hashed with the sha256 algorithm
		sha = hasher.sha256()
		seq = (str(x) for x in (
			   self.index, self.timestamp, self.data, self.previous_hash))

		# Makes sure it's encode in utf-8
		sha.update(''.join(seq).encode('utf-8'))

		# returns the combined hash value in Hexadecimals
		return sha.hexdigest()

def make_genesis_block():
	# Makes the first block in the BDC blockchain.
	block = BDBlock(index=0,
					timestamp=datetime.now(),
					data="Genesis Block",
					previous_hash="0")
	return block