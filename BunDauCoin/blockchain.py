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
