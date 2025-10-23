from pydantic import BaseModel

# @todo create other ontology components
class Class(BaseModel):
    label: str
    members: list

class Property(BaseModel):
    domain: str # create class concept
    range: str
    property: str


class BlankNode(BaseModel):
    # blanc node description as text
    intersection: bool
    conjunction : bool


