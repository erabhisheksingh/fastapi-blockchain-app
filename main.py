from typing import List

from fastapi import FastAPI, HTTPException, status

from blocks import block
from models import blockmodel

app = FastAPI()

blockchain = block.Blockchain()

@app.get("/blocks/mine", status_code=status.HTTP_200_OK, response_model=blockmodel.Block, tags=['Blocks'])
def mine_block():
    
    """
    This function is used to mine a block for the Blockchain 
    """
    return blockchain.create_block()

@app.get("/blocks/all", status_code=status.HTTP_200_OK, response_model=List[blockmodel.Block], tags=['Blocks'])
def all_blocks():
    
    """
    This function is used to get all the blocks in the Blockchain 
    """ 
    blocks = blockchain.blockchain
    if len(blocks) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blocks not found")
    return blocks

@app.get("/blocks/{id}", status_code=status.HTTP_200_OK, response_model=blockmodel.Block, tags=['Blocks'])
def get_blocks(id: int):
    
    """
    This function is used to get a particular block in the Blockchain 
    """ 
    block = blockchain.blockchain[id]
    if not block:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Block with the Id - {id} not found")
    return block
