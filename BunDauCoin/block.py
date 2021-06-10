import hashlib

from flask import current_app, g

class Block:

    def __init__(self, index, previousHash, timestamp, data):
        self.index = index;
        self.previousHash = previousHash;
        self.timestamp = timestamp;
        self.data = data;
        self.hash = self.calculateHash;

    def calculateHash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data))
        return sha.hexdigest()