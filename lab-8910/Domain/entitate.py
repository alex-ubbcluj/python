from abc import ABC
from dataclasses import dataclass


@dataclass
class Entitate(ABC):
    """
    Descrie o entitate
    """
    id_entitate: str
