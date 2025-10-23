from typing import List
from pandas.core.common import not_none
from pydantic import BaseModel


class Isa(BaseModel):
    """
    Il est demandé d'énumérer les GENERIQUES/hyperonymes du terme.
    """
    source: str
    cible: str
    relation_type: str ="r_isa"
    jdm_id: int = 6


class HasPart(BaseModel):
    source: str
    cible: str
    relation_type: str = "r_has_part"
    jdm_id: int = 9


class Mater(BaseModel):
    """
    Pour un terme donné, souvent un objet, il est demandé d'en énumérer les caractéristiques (adjectifs)
    possibles/typiques.
    """
    source: str
    cible: str
    relation_type: str = "r_object>mater"
    jdm_id: int = 50


class Carac(BaseModel):
    """
    Pour un terme donné, souvent un objet, il est demandé d'en énumérer les caractéristiques (adjectifs)
    possibles/typiques.
    """
    source: str
    cible: str
    relation_type: str = "r_carac"
    jdm_id: int = 17


class Color(BaseModel):
    """
    A comme couleur(s).
    """
    source: str
    cible: str
    relation_type: str = "r_has_color"
    jdm_id: int = 106


class Processus(BaseModel):
    """
    Pour un terme donné, souvent un objet, il est demandé d'en énumérer les caractéristiques (adjectifs)
    possibles/typiques.
    """
    source: str
    cible: str
    relation_type: str = "r_processus>patient-1"
    jdm_id: int = 138


class Lieu(BaseModel):
    """
    Il est demandé d'énumérer les LIEUX typiques où peut se trouver le terme/objet en question.
    """
    source: str
    cible: str
    relation_type: str = "r_lieu"
    jdm_id: int = 15


class Syn(BaseModel):
    """
    Il est demandé d'énumérer les synonymes ou quasi-synonymes de ce terme.
    """
    source: str
    cible: str
    relation_type: str = "r_syn"
    jdm_id: int = 5


# ok
class IsaRelations(BaseModel):
    relations: List[Isa]

# ok
class HasPartRelations(BaseModel):
    relations: List[HasPart]

#ok
class MaterRelations(BaseModel):
    relations: List[Mater]

#ok
class CaracRelations(BaseModel):
    relations: List[Carac]

#ok
class ColorRelations(BaseModel):
    relations: List[Color]

#ok
class ProcessusRelations(BaseModel):
    relations: List[Processus]

#ok
class LieuRelations(BaseModel):
    relations: List[Lieu]

#ok
class SynRelations(BaseModel):
    relations: List[Syn]



# ----------------------- for later use -------------------------------



class Locution(BaseModel):
    """
    A partir d'un terme, il est demandé d'énumérer les locutions, expression ou mots composés en rapport avec ce terme.
    """
    source: str
    cible: str
    relation_type: str = "r_locution"
    jdm_id: int = 11


class Instr(BaseModel):
    """
    L'instrument est l'objet avec lequel on fait l'action.
    """
    source: str
    cible: str
    relation_type: str = "r_instr"
    jdm_id: int = 16


class Manner(BaseModel):
    """
    De quelles manières peut être effectuée l'action (le verbe) proposée.
    Il s'agira d'un adverbe ou d'un équivalent comme une locution adverbiale
    """
    source: str
    cible: str
    relation_type: str = "r_manner"
    jdm_id: int = 34



class InstrRelations(BaseModel):
    relations: List[Lieu]

class LocutionRelations(BaseModel):
    relations: List[Locution]

class MannerRelations(BaseModel):
    relations: List[Manner]

# ---------------------------------------------------------------------




