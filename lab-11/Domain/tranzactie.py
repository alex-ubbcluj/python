from dataclasses import dataclass
from Domain.entity import Entity


@dataclass
class Tranzactie(Entity):
    id_client_sursa: str
    id_client_destinatie: str
    valoare: float
