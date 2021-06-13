from flask import current_app, g
from flask.cli import with_appcontext

import datetime
import hashlib

from . import block
from . import db

"""
    +===========================+
    |   Making the Blockchain   |
    +===========================+
"""

##
## Create Genesis block of the chain
##
## :returns:   Return the created genesis block
## :rtype:     block.Block
##
def genesisBlock() -> block.Block:
    return block.Block(
        index=0, 
        previousHash="0", 
        timestamp=int(datetime.datetime.now().timestamp()), 
        data="Genesis Bun Dau Block"
    )

##
## Generate a new block for the chain
##
## :param      blockData:  Data to feed the block
## :type       blockData:  str
##
## :returns:   The new block for the chain
## :rtype:     block.Block
##
def generateNextBlock(blockData: str) -> block.Block:
    previousBlock = self.getLatestBlock()
    return block.Block(
        index=previousBlock.index+1,
        previousHash=previousBlock.hash, 
        timestamp=int(datetime.datetime.now().timestamp()), 
        data=blockData
    )

"""
    +=============================+
    |   Checking the Blockchain   |
    |    integrity                |
    +=============================+
"""

##
## Determines if valid new block.
##
## :param      newBlock:       The new block
## :type       newBlock:       block.Block
## :param      previousBlock:  The previous block
## :type       previousBlock:  block.Block
##
## :returns:   True if valid new block, False otherwise.
## :rtype:     bool
##
def isValidNewBlock(newBlock: block.Block, previousBlock: block.Block) -> bool:
    result = False
    if previousBlock.index + 1 == newBlock.index:
        if previousBlock.hash == newBlock.previousHash:
            if block.Block.calculateHash(newBlock) == newBlock.hash:
                result = True
    
    return result
##
## Determines whether the specified block is valid block structure.
##
## :param      block:  The block
## :type       block:  block.Block
##
## :returns:   True if the specified block is valid block structure, False otherwise.
## :rtype:     bool
##
def isValidBlockStructure(block: block.Block):
    return (isinstance(block.index, int) 
        and isinstance(block.hash, str) 
        and isinstance(block.previousHash, str) 
        and isinstance(block.timestamp, datetime.datetime)
        and isinstance(block.data, str)
    )
