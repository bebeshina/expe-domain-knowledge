from typing import List
from pydantic import BaseModel


class Link(BaseModel):
    node_1: str
    node_2: str
    weight: float


class Links(BaseModel):
    links: List[Link]


class Isa(BaseModel):
    """
    Il est demandé d'énumérer les GENERIQUES/hyperonymes du terme.
    """
    source: str
    cible: str
    # relation_type: str ="r_isa"
    w: int
    # jdm_id: int = 6

class Relation(BaseModel):
    """
    Il est demandé d'énumérer les GENERIQUES/hyperonymes du terme.
    """
    source: str
    target: str
    relation_type: str
    poids: float
    # jdm_id: int = 6


class Relations(BaseModel):
    relations: List[Relation]