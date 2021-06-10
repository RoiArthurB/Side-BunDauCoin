from flask import current_app, g
from flask.cli import with_appcontext

import datetime
import hashlib

from . import block

"""
    +===========================+
    |   Making the Blockchain   |
    +===========================+
"""

##
## { function_description }
##
## :returns:   { description_of_the_return_value }
## :rtype:     { return_type_description }
##
def genesisBlock():
    return block.Block(
        index=0, 
        previousHash="0", 
        timestamp=datetime.datetime.now(), 
        data="Genesis Bun Dau Block"
    )

##
## { function_description }
##
## :param      blockData:  The block data
## :type       blockData:  { type_description }
##
## :returns:   { description_of_the_return_value }
## :rtype:     { return_type_description }
##
def generateNextBlock(blockData):
    previousBlock = self.getLatestBlock()
    return block.Block(
        index=previousBlock.index+1,
        previousHash=previousBlock.hash, 
        timestamp=datetime.datetime.now(), 
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
## :type       newBlock:       { type_description }
## :param      previousBlock:  The previous block
## :type       previousBlock:  { type_description }
##
## :returns:   True if valid new block, False otherwise.
## :rtype:     bool
##
def isValidNewBlock(newBlock, previousBlock):
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
## :type       block:  { type_description }
##
## :returns:   True if the specified block is valid block structure, False otherwise.
## :rtype:     bool
##
def isValidBlockStructure(block):
    return (isinstance(block.index, int) 
        and isinstance(block.hash, str) 
        and isinstance(block.previousHash, str) 
        and isinstance(block.timestamp, datetime.datetime)
        and isinstance(block.data, str)
    )