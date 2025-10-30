from typing import List, Any
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
    # __pydantic_custom_init__ = True
    def __get_relation_list__(self, relations):
        return self.relations

    def __set_relation_list__(self, relation_list: list):
        self.relations = relation_list
        return 0
    #
    # def __call__(self, relations: list):
    #     self.relations = relations
    #
    # def __init__(self, relations: list, /, **data: Any):
    #     super().__init__(**data)
    #     self.relations = relations