from dataclasses import dataclass
from Domain.entity import Entity


@dataclass
class Client(Entity):
    nume: str
    cnp: str
    sold_initial: float
