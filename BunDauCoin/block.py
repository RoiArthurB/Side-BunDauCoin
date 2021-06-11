from flask import current_app, g

import hashlib

class Block:

    def __init__(self, index: int, previousHash: str, timestamp, data: str):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculateHash()

    def calculateHash(self) -> str:
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') + str(self.previousHash).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8'))
        return sha.hexdigest()