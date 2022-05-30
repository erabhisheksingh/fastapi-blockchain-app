import hashlib
import json
from datetime import datetime as dt

from models import blockmodel


class Blockchain:
    """
    Blockchain class having the functions to operate on a Block.
    """
    
    
    def __init__(self):
        """
        This function is used to initialize a Block 
        """
        
        self.blockchain = []
        self.create_block()
        
    def create_block(self):
        """
        This function is used to create a new Block 
        """
        
        if len(self.blockchain) > 1:
            prev_block = self.get_prev_block()
            result = self.proof_of_work(prev_block["nonce"])
            block = {
                "index": len(self.blockchain) + 1,
                "timestamp": str(dt.now()),
                "nonce": result[0],
                "current_hash": result[1],
                "previous_hash": prev_block["current_hash"]
            }
        else:
            result = self.proof_of_work(0)
            block = {
                "index": len(self.blockchain) + 1,
                "timestamp": str(dt.now()),
                "nonce": result[0],
                "current_hash": result[1],
                "previous_hash": "00000000000000000"
            }
        self.blockchain.append(block)
        return block
    
    def get_prev_block(self):
        """
        This function is used to get the previous Block 
        """
         
        return self.blockchain[-1]
    
    @staticmethod
    def proof_of_work(prev_nonce: int):
        """
        This function is used to get the proof of work for a Block 
    
        Parameters
        ----------
        prev_nonce : int
            The previous Block nonce value
        """
         
        nonce = 1
        check_nonce = False
        result = []
        while check_nonce is False:
            hash_operation = hashlib.sha256(str(nonce**2 - prev_nonce**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nonce = True
                result.append(nonce)
                result.append(hash_operation)
            else:
                nonce += 1
        return result
    
    @staticmethod
    def hash(block: blockmodel.Block):
        """
        This function is used to get the hash for the input Block 
    
        Parameters
        ----------
        block : blockmodel.Block
            The Block to get the Hash
        """
        
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()    
