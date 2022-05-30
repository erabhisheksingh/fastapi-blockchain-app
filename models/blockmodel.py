from typing import Optional

from pydantic import BaseModel


class Block(BaseModel):

    """
    This class is the Base class for the Block object
    
    ...

    Attributes
    ----------
    index : int
        the index of the Block
    timestamp : str
        the timestamp when the Block was created
    nonce : int
        the nonce of the Block
    current_hash : str
        the current hash of the Block
    previous_hash : Optional[str]
        the previous_hash of the Block

    """
    
    index: int
    timestamp: str
    nonce: int
    current_hash: str
    previous_hash: Optional[str] = None
    
    

