from flask import current_app, g

import hashlib

##
## This class describes a block.
##
class Block:
    ##
    ## Constructs a new instance.
    ##
    ## :param      index:         The index
    ## :type       index:         int
    ## :param      previousHash:  The previous hash
    ## :type       previousHash:  str
    ## :param      timestamp:     The timestamp the block has been created at
    ## :type       timestamp:     int
    ## :param      data:          The data
    ## :type       data:          str
    ## :param      hash:          The hash
    ## :type       hash:          str
    ##
    def __init__(self, index: int, previousHash: str, timestamp: int, data: str, hash: str = ""):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        if hash == "":
            self.hash = self.calculateHash()
        else:
            self.hash = hash

    ##
    ## Calculates the hash.
    ##
    ## :returns:   The hash.
    ## :rtype:     str
    ##
    def calculateHash(self) -> str:
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') + str(self.previousHash).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8'))
        return sha.hexdigest()

    """
        +=====================+
        |   Getter / Setter   |
        +=====================+
    """
    ##
    ## Gets the index.
    ##
    ## :returns:   The index.
    ## :rtype:     int
    ##
    def getIndex(self) -> int:
        return int(self.index)
    
    ##
    ## Gets the previous hash.
    ##
    ## :returns:   The previous hash.
    ## :rtype:     str
    ##
    def getPreviousHash(self) -> str:
        return self.previousHash
    
    ##
    ## Gets the hash.
    ##
    ## :returns:   The hash.
    ## :rtype:     str
    ##
    def getHash(self) -> str:
        return self.hash
    
    ##
    ## Gets the timestamp.
    ##
    ## :returns:   The timestamp.
    ## :rtype:     int
    ##
    def getTimestamp(self) -> int:
        return self.timestamp
    
    ##
    ## Gets the data.
    ##
    ## :returns:   The data.
    ## :rtype:     str
    ##
    def getData(self) -> str:
        return self.data